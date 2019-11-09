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
def lsi_tfidf():
    from gensim import corpora, models, similarities
    import jieba
    text = ''
    text1 = '有时公众会误以为计算机科学就是解决计算机问题的事业（比如信息技术），或者只是与使用计算机的经验有关，如玩游戏、上网或者文字处理。其实计算机科学所关注的不仅仅是去理解实现类似游戏、浏览器这些软件的程序的性质，更是通过利用现有的知识创造新的程序或者改进已有的程序。计算机科学与技术是研究计算机的设计与制造，利用计算机进行信息获取、表示、存储、处理、控制等的理论、原则、方法和技术的专业。'
    text2 = '计算机（computer）俗称电脑，是现代一种用于高速计算的电子计算机器，可以进行数值计算，又可以进行逻辑计算，还具有存储记忆功能。是能够按照程序运行，自动、高速处理海量数据的现代化智能电子设备。由硬件系统和软件系统所组成，没有安装任何软件的计算机称为裸机。可分为超级计算机、工业控制计算机、网络计算机、个人计算机、嵌入式计算机五类，较先进的计算机有生物计算机、光子计算机、量子计算机等。计算机发明者约翰·冯·诺依曼。计算机是20世纪最先进的科学技术发明之一，对人类的生产活动和社会活动产生了极其重要的影响，并以强大的生命力飞速发展。它的应用领域从最初的军事科研应用扩展到社会的各个领域，已形成了规模巨大的计算机产业，带动了全球范围的技术进步，由此引发了深刻的社会变革，计算机已遍及一般学校、企事业单位，进入寻常百姓家，成为信息社会中必不可少的工具。'
    text3 = '计算机技术在高峰论坛上发表技术演讲，有关计算机的程序包括游戏，上网，处理文字等内容？'
    keyword = '他指出，IPv6是中国参与全球互联网技术发展的重要契机。未来互联网的挑战将集中体现在互联网体系结构的研究和发展上。在2019全国高等教育信息化高峰论坛上，中国工程院院士、清华大学教授吴建平作了《构筑先进安全的国家高等教育和科技创新信息化基础设施》的主题发言。'
    texts = [text1, text2, keyword, text3]

    # print(texts)
    texts = [jieba.lcut(text) for text in texts]
    # print(texts)
    dictionary = corpora.Dictionary(texts)
    # print(dictionary.token2id,'guoshengwei')
    num_features = len(dictionary.token2id)
    # print(num_features)
    corpus = [dictionary.doc2bow(text) for text in texts]
    # print(corpus,'corpus')
    tfidf = models.TfidfModel(corpus)
    # print(tfidf,'tfidf')
    new_vec = dictionary.doc2bow(jieba.lcut(keyword))
    # print(new_vec,'new_vec')
    # 相似度计算
    # print(tfidf[corpus][1],'tidf[corpus]')
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features)
    print('\nTF-IDF模型的稀疏向量集：')
    # for i in tfidf[corpus]:
    #    print(i)
    print('\nTF-IDF模型的keyword稀疏向量：')
    # print(tfidf[new_vec])
    print('\nTFidf相似度计算：')
    sim = index[tfidf[new_vec]]
    # print(sim)
    for i in range(len(sim)):
        print('第', i + 1, '句话的相似度为：', sim[i])
        if sim[i] > 0.5:
            print('第', i + 1, '句话的相似度为：', sim[i], '相似度为：', sim[i] / 1 * 100, '%')
    lsi = models.LsiModel(tfidf[corpus], id2word=dictionary, num_topics=tfidf.num_docs)
    index1 = similarities.MatrixSimilarity(lsi[tfidf[corpus]])
    sims = index1[lsi[tfidf[new_vec]]]
    print('Lsi相似度', sims)
    for u in range(len(sims)):
        print('第', u + 1, '段的相似度为：', sims[u])
        if sims[u] > 0.5:
            print('第', u + 1, '段的相似度为：', sims[u], '相似度为：', sims[u] / 1 * 100, '%')
