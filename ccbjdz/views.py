from django.shortcuts import render
from django.views.generic import ListView
from ccbjdz.models import Worksheet
from django.db.models import Count
from django.shortcuts import render, HttpResponse, redirect
from django.db.models import F, Q
from ccbjdz.page import Pagination, PaginationQuery


# Create your views here.
class CommonListCcbjdz:
    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)
        contexts.update(
            {'allorganization': Worksheet.objects.values('filloutorganization').annotate(
                Count('filloutorganization')).order_by()})

        return contexts


class CcbjdzListview(ListView):
    model = Worksheet
    template_name = 'templatesccb/detail_list.html'
    context_object_name = 'detail_list'
    paginate_by = 10


class ccbjdzListchoice(CcbjdzListview):
    def get_queryset(self):
        qs = super().get_queryset().order_by('date')
        select_content = qs.filter(id=self.request.GET.get('id')).values()
        return select_content


# def issueIndex(request):
#     issues = Worksheet.objects.all().order_by('id')
#     issues1= Worksheet.objects.values('filloutorganization').annotate(
#                 Count('filloutorganization')).order_by()
#     # 分页
#     currentPage = int(request.GET.get("p", 1))  # 当前页，如果没有默认1
#     perPageCnt = 15  # 每页显示10个数据
#     totalCnt = Worksheet.objects.all().count()  # 获取全部数据个数
#     pageIndexCnt = 6  # 显示页码 5个,
#     pagination = Pagination(currentPage, perPageCnt, totalCnt, pageIndexCnt, request.path)
#
#     if currentPage > 0 and currentPage < pagination.page_nums:
#         issues = issues[pagination.startNum:pagination.endNum]
#     elif currentPage == pagination.page_nums:
#         issues = issues[pagination.startNum::]
#     else:
#         issues = issues[0:10]
#     return render(request, "templatesccb/jdzpage.html", {"issues": issues, "pagination": pagination,'allorganization':issues1})


def seleIssue(request):  #根据条件选择需要的内容
    content = request.GET.get("content", None)
    issues1 = Worksheet.objects.values('filloutorganization').annotate(
        Count('filloutorganization')).order_by()
    # 判断是否有查询内容
    if content:
        issues = Worksheet.objects.filter(Q(filloutorganization=content)).order_by('id')  #条件选择
    else:
        issues = Worksheet.objects.all().order_by('id') #如果没有条件选择全部
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

    return render(request, "templatesccb/jdzpage.html", {"issues": issues, "pagination": pagination,'allorganization':issues1})