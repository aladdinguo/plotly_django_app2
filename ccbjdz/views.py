from django.shortcuts import render
from django.views.generic import ListView
from ccbjdz.models import Worksheet
from django.db.models import Count
from django.shortcuts import render, HttpResponse, redirect
from django.db.models import F, Q
from ccbjdz.page import Pagination, PaginationQuery
import codecs
import jieba.posseg as psg
import jieba
from gensim import corpora, models, similarities


# Create your views here.
class CommonListCcbjdz:
    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)
        contexts.update(
            {'allorganization': Worksheet.objects.values('filloutorganization').annotate(
                Count('filloutorganization')).order_by()})
        return contexts


class CcbjdzListview(CommonListCcbjdz, ListView):
    model = Worksheet
    template_name = 'templatesccb/detail_list.html'
    context_object_name = 'detail_list'
    paginate_by = 10


class ccbjdzListchoice(CcbjdzListview):
    def get_queryset(self):
        qs = super().get_queryset().order_by('date')
        select_content = qs.filter(id=self.request.GET.get('id')).values()
        # print('aaa',type(select_content[0]),'aaa')
        # print(select_content[0].get('id'))
        # print(select_content[0].get('describe'))
        print(select_content[0].get('createidentification'))
        #下面内容是把describe字段的内容转化成词袋模型存储到数据库中
        if select_content[0].get('createidentification') == None:
            Worksheet.objects.filter(id=select_content[0].get('id')).update(
                createidentification=similarcompare.tokenization_trainverctor(select_content[0].get('describe')))

        return select_content


def seleIssue(request):  # 根据条件选择需要的内容
    content = request.GET.get("content", None)
    issues1 = Worksheet.objects.values('filloutorganization').annotate(
        Count('filloutorganization')).order_by()
    # 判断是否有查询内容
    if content:
        issues = Worksheet.objects.filter(Q(filloutorganization=content)).order_by('id')  # 条件选择
    else:
        issues = Worksheet.objects.all().order_by('id')  # 如果没有条件选择全部
    # 分页显示
    currentPage = int(request.GET.get("p", 1))  # 当前页，如果没有默认1
    perPageCnt = 15  # 每页显示10个数据
    totalCnt = issues.count()  # 获取全部数据个数
    pageIndexCnt = 6  # 显示页码 5个,
    print(currentPage, "currentpage", totalCnt, pageIndexCnt, request.path)
    # 判断是否有查询，如果没有就取全部index即可（调用PaginationQuery），如果有内容就调用PaginationQuery
    if content:
        pagination = PaginationQuery(currentPage, perPageCnt, totalCnt, pageIndexCnt, request.path, content)
    else:
        pagination = Pagination(currentPage, perPageCnt, totalCnt, pageIndexCnt, request.path)
    # 获取当前页面要显示的内容，使用切片模式
    if currentPage > 0 and currentPage < pagination.page_nums:
        issues = issues[pagination.startNum:pagination.endNum]
    elif currentPage == pagination.page_nums:
        issues = issues[pagination.startNum::]
    else:
        issues = issues[0:10]

    return render(request, "templatesccb/jdzpage.html",
                  {"issues": issues, "pagination": pagination, 'allorganization': issues1})


def txtcampare(self, **kwargs):
    from gensim import corpora, models, similarities
    from collections import defaultdict
    # 用于创建一个空的字典，在后续统计词频可清理频率少的词语
    # 1、读取文档
    # doc1="./d1.txt"
    # doc2="./d2.txt"
    d1 = "目前，我行点钞机有的是中钞信达，有的是聚龙，但这些点钞机仍存在一些瑕疵，定期需要厂家维修保养，同时过钱后灰尘较大，众所周知，柜员是辛苦的服务人员，每天要面对不停的现金，日前，网点接待某位客户的20万存款，均是长期受潮且发霉的现金，柜员过钱时灰尘都冒烟，同时还伴有酸臭味道。业务办理结束后，柜员的桌子上，衣服上甚至头发上都是灰尘。"
    d2 = "由于身份证有使用期限，办理新身份证要等待时间，时间较长，客户需要等待，所以会有临时身份证的使用。还有未成年人拿户口本办业务.而有些客户办业务时，再走远程授权时，会拍摄交易场景的照片，在1019身份核查拍摄时，还会显示清晰度。如果清晰度不够可以重新拍摄，而在远程中的交易场景拍照里不显示，多次退回因为拍摄不清楚，客户也会有怨言。"
    # 2、对要计算的文档进行分词
    data1 = jieba.cut(d1)
    data2 = jieba.cut(d2)
    # 3、对分词完的数据进行整理为指定格式
    data11 = ""
    for i in data1:
        data11 += i + " "
    print(data11)
    data21 = ""
    for i in data2:
        data21 += i + " "
    documents = [data11, data21]
    texts = [[word for word in document.split()] for document in documents]
    print(texts)
    # 4、 计算词语的频率
    frequency = defaultdict(int)
    for text in texts:
        for word in text:
            frequency[word] += 1
    print(frequency)
    '''
    #5、对频率低的词语进行过滤（可选）
    texts=[[word for word in text if frequency[word]>10] for text in texts]
    '''
    # 6、通过语料库将文档的词语进行建立词典
    dictionary = corpora.Dictionary(texts)
    dictionary.save("./dict.txt")  # 可以将生成的词典进行保存
    # 7、加载要对比的文档
    # doc3="./d3.txt"
    d3 = "目前我行已实现柜面客户取号自动商机推荐和智慧机平板电脑和建行员工ap的商机推荐，但是在智慧柜员机渠道希望新增客户营销商机推荐，如在客户办理业务结束页面增加客户商机推荐，联动营销，增强营销成功率。在智慧柜员机结束页面也不会影响客户办理业务，也不会降低客户体验，相反可以增加我行的产品覆盖度和客户营销。"
    data3 = jieba.cut(d3)
    data31 = ""
    for i in data3:
        data31 += i + " "
    # 8、将要对比的文档通过doc2bow转化为稀疏向量
    new_xs = dictionary.doc2bow(data31.split())
    # 9、对语料库进一步处理，得到新语料库
    corpus = [dictionary.doc2bow(text) for text in texts]
    # 10、将新语料库通过tf-idf model 进行处理，得到tfidf
    tfidf = models.TfidfModel(corpus)
    # 11、通过token2id得到特征数
    featurenum = len(dictionary.token2id.keys())
    # 12、稀疏矩阵相似度，从而建立索引
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=featurenum)
    # 13、得到最终相似结果
    sim = index[tfidf[new_xs]]
    print(sim)


class similarcompare(ccbjdzListchoice):

    def tokenization_trainverctor(txt):
        textall = [txt]
        print(textall)
        stopwords = codecs.open('static/text/stopwords.txt',
                                'r', encoding='utf8').readline()  # 读取停用词
        stopwords = [w.strip() for w in stopwords]
        stop_flag = ['x', 'c', 'u', 'd', 'p', 't', 'uj', 'm', 'f', 'r', 'y']
        all_doc_list = []
        for doc in textall:
            print(doc)
            result = []
            for word, flag in psg.cut(doc):
                if flag not in stop_flag and word not in stopwords:
                    result.append(word)
            all_doc_list.append(result)
        dictionary = corpora.Dictionary(all_doc_list)
        doc_vectors = [dictionary.doc2bow(text) for text in all_doc_list]
        for delete_code in doc_vectors:
            doc_vectors_N=delete_code
        return doc_vectors_N

    def update_record(self):
        counts = Worksheet.objects.all().count()
        for record in Worksheet.objects.values_list('id', 'describe', 'createidentification'):
            if record.createidentification != None and record[0] == 1:
                Worksheet.objects.filter(id=record[0]).update(
                    createidentification=similarcompare.tokenization_trainverctor(record[1]))
