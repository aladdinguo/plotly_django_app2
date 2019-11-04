from django.test import TestCase
from ccbjdz.models import Worksheet
from django.shortcuts import  render
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
#调用func函数去除重复的字符后，在写入数据表中。
    list1 = Worksheet.objects.values_list('id', 'creativitylightspot', 'describe', 'modusoperandi', 'benefitestimate')
    for words in list1:
        if words[1] != None:
            Worksheet.objects.filter(id=words[0]).update(creativitylightspot=func(words[1]))
        if words[2] != None:
            Worksheet.objects.filter(id=words[0]).update(describe=func(words[2]))
        if words[3] != None:
            Worksheet.objects.filter(id=words[0]).update(modusoperandi=func(words[3]))
        if words[4] != None:
            Worksheet.objects.filter(id=words[0]).update(benefitestimate=func(words[4]))
    return render(request, 'templatesccb/jdzpage.html')