from django.test import TestCase
from ccbjdz.models import Worksheet
from django.shortcuts import render
import jieba
from gensim import corpora, models, similarities
import codecs


# Create your tests here.

def func(_str):  # 数据清洗，去掉连续重复的字符串
    _list = list(_str)
    n = len(_list)
    if n <= 1:
        return
    list1 = []
    for i in range(n - 1):
        if _list[i] != _list[i + 1]:
            list1.append(_list[i])
    list1.append(_list[-1])
    str1 = ''.join(list1)
    return str1


def readdataworksheet(request):
    # 调用func函数去除重复的字符后，在写入数据表中。
    list1 = Worksheet.objects.values_list('id', 'creativitylightspot', 'describe', 'modusoperandi', 'benefitestimate')
    # for words in list1:
    #     if words[1] != None:
    #         Worksheet.objects.filter(id=words[0]).update(creativitylightspot=func(words[1]))
    #     if words[2] != None:
    #         Worksheet.objects.filter(id=words[0]).update(describe=func(words[2]))
    #     if words[3] != None:
    #         Worksheet.objects.filter(id=words[0]).update(modusoperandi=func(words[3]))
    #     if words[4] != None:
    #         Worksheet.objects.filter(id=words[0]).update(benefitestimate=func(words[4]))
    return render(request, 'templatesccb/jdzpage.html')


class textduibi:

    def cut_words(file):
        with open(file, 'r', encoding="utf-8") as f:
            text = f.read()
            words = jieba.lcut(text)
            # print(len(words),words) #查看分词结果
        return words

    def drop_Disable_Words(cut_res, stopwords):
        res = []
        for word in cut_res:
            if word in stopwords or word == "\n" or word == "\u3000":
                continue
            res.append(word)
        # print(len(res),res) #查看去停用词结果
        return res

    def read_stop_word(file_path):
        file = file_path
        stopwords = codecs.open(file, 'r', encoding='utf8').readlines()
        stopwords = [w.strip() for w in stopwords]
        return stopwords

    # 读取原始语料、停用词表
    files = ['file1.txt',
             'file2.txt',
             'file3.txt'
             ]
    stopwords = read_stop_word("stop_word.txt")

    # 分词、去停用词
    corpus = []
    for file in files:
        # 分词
        cut_res = cut_words(file)
        # 去停用词
        res = drop_Disable_Words(cut_res, stopwords)
        corpus.append(res)
    # print(len(corpus))

    # 建立词袋模型
    dictionary = corpora.Dictionary(corpus)
    doc_vectors = [dictionary.doc2bow(text) for text in corpus]
    # print(len(doc_vectors),doc_vectors)
    #####################################################################
    # print("文档数目:")
    # print (dictionary.num_docs)
    #
    # print("所有词的个数:")
    # print(dictionary.num_pos )
    #
    # print("单词在文档中出现的次数：")
    # print(dictionary.dfs )
    #
    # print("字典，{单词id:对应的词}")
    # print((dictionary.id2token))
    #
    # print ("字典，{词:对应的单词id}")
    # print((dictionary.token2id))

    # print ("每个文件中不重复词个数的和")
    # print(dictionary.num_nnz)  #每个文件中不重复词个数的和
    ##########################################################################

    tfidf = models.TfidfModel(doc_vectors)
    tfidf_vectors = tfidf[doc_vectors]
    print(len(tfidf_vectors))
    print(len(tfidf_vectors[0]))
    print(tfidf_vectors[0])

    # 建立TF-IDF模型
    def TF_IDF(tfidf_vectors, doc_vectors):
        index = similarities.MatrixSimilarity(tfidf_vectors)
        sims = index[doc_vectors[0]]
        print(list(enumerate(sims)))

    # 建立LSI模型
    def LSI(tfidf_vectors, dictionary, doc_vectors, theme_num):
        lsi = models.LsiModel(tfidf_vectors, id2word=dictionary, num_topics=theme_num)
        lsi_vector = lsi[tfidf_vectors]
        query_lsi = lsi[doc_vectors[0]]
        index = similarities.MatrixSimilarity(lsi_vector)
        sims = index[query_lsi]
        print(list(enumerate(sims)))

    # 使用LSI模型计算相似度
    LSI(tfidf_vectors, dictionary, doc_vectors, 2)

    # 使用TF-IDF模型计算相似度
    TF_IDF(tfidf_vectors, doc_vectors)
