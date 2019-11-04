# 适用于妹子UI的分页前端
# 适用于所有数据分页，普通分页
class Pagination(object):
    # totalCnt代表表单内容总数量
    def __init__(self, currentPage, perPageCnt, totalCnt, pageIndexCnt, urls):
        self.currentPage = currentPage
        self.perPageCnt = perPageCnt
        self.totalCnt = totalCnt
        self.pageIndexCnt = pageIndexCnt  # 表示分页索引显示几个页面，一般显示5个
        self.urls = urls

    # 加上@property时，调用方法不用加()
    @property
    def page_nums(self):
        if self.totalCnt % self.perPageCnt == 0:
            return int(self.totalCnt / self.perPageCnt)
        else:
            return int(self.totalCnt / self.perPageCnt) + 1

    # 其实条数，切片用
    @property
    def startNum(self):
        return (self.currentPage - 1) * self.perPageCnt

    @property
    def endNum(self):
        return self.currentPage * self.perPageCnt

    @property
    def prevPage(self):
        return self.currentPage - 1

    @property
    def nextPage(self):
        return self.currentPage + 1

    # 分页显示页码，比如显示: prev<< 4,5,6,7,8 >>next
    @property
    def pageRange(self):
        part = int(self.pageIndexCnt / 2)
        if self.pageIndexCnt < self.page_nums:
            if self.currentPage < int(self.pageIndexCnt / 2 + 1):
                return range(1, self.pageIndexCnt + 1)
            elif self.currentPage > self.page_nums - part:
                return range(self.page_nums - self.pageIndexCnt, self.page_nums + 1)
            else:
                return range(self.currentPage - part, self.currentPage + part + 1)
        else:
            return range(1, self.page_nums + 1)

    # 直接输送代码给模板
    @property
    def pageStr(self):
        pageNumStr = []
        prev_page = ""
        next_page = ""
        # 页码
        if self.currentPage > 1 and self.currentPage < self.page_nums:
            prev_page = "<td><a href=" + self.urls + "?p=%s>&laquo; 前一页</a></td>" % (self.currentPage - 1)
            next_page = "<td><a href=" + self.urls + "?p=%s> 后一页&raquo;</a></td>" % (self.currentPage + 1)
        if self.currentPage == self.page_nums:
             prev_page = "<td class='am-disabled'><a href=" + self.urls + "?p=%s>&laquo; 前一页</a></td>"% (self.currentPage - 1)
        if self.currentPage == 1:
             next_page = "<td class='am-disabled'><a href=" + self.urls + "?p=%s>后一页 &raquo;</a></td>" % (self.currentPage + 1)

        for page in self.pageRange:
            if page == self.currentPage:
                pageNumStr.append("<td class='am-active'><span class='label label-important'><a href=" + self.urls + "?p=%s>%s</a></span></td>" % (page, page))
            else:
                pageNumStr.append("<td><span class='label label-important'><a href=" + self.urls + "?p=%s>%s</a></span></td>" % (page, page))
            print(pageNumStr)

        return prev_page + "".join(pageNumStr) + next_page


# 适用于妹子UI的分页前端
# 对已经分页的数据进行查询，对查询后的数据再次进行分页
# 思路：url请求除了需要带current page 还需要带查询的内容
class PaginationQuery(object):
    # content代表需要查询的关键字
    def __init__(self, currentPage, perPageCnt, totalCnt, pageIndexCnt, urls, content):
        self.currentPage = currentPage  # 当前页码
        self.perPageCnt = perPageCnt  # 每页要显示多少条
        self.totalCnt = totalCnt  # totalCnt代表表单内容总数量
        self.pageIndexCnt = pageIndexCnt  # 表示分页索引显示几个页面，一般显示5个
        self.urls = urls  # 请求路径
        self.content = content  # 查询关键字

    # 加上@property时，调用方法不用加()
    @property
    def page_nums(self):
        if self.totalCnt % self.perPageCnt == 0:
            return int(self.totalCnt / self.perPageCnt)
        else:
            return int(self.totalCnt / self.perPageCnt) + 1

    # 其实条数，切片用
    @property
    def startNum(self):
        return (self.currentPage - 1) * self.perPageCnt

    @property
    def endNum(self):
        return self.currentPage * self.perPageCnt

    @property
    def prevPage(self):
        return self.currentPage - 1

    @property
    def nextPage(self):
        return self.currentPage + 1

    # 分页显示页码，比如显示: prev<< 4,5,6,7,8 >>next
    @property
    def pageRange(self):
        part = int(self.pageIndexCnt / 2)
        if self.pageIndexCnt < self.page_nums:
            if self.currentPage < int(self.pageIndexCnt / 2 + 1):
                return range(1, self.pageIndexCnt + 1)
            elif self.currentPage > self.page_nums - part:
                return range(self.page_nums - self.pageIndexCnt, self.page_nums + 1)
            else:
                return range(self.currentPage - part, self.currentPage + part + 1)
        else:
            return range(1, self.page_nums + 1)

    # 直接输送代码给模板
    @property
    def pageStr(self):
        pageNumStr = []
        prev_page = ""
        next_page = ""
        # 页码
        if self.currentPage > 1 and self.currentPage < self.page_nums:
            prev_page = "<td><a href=" + self.urls + "?p=%s&content=%s>&laquo; 前一页</a></td>" % (
            self.currentPage - 1, self.content)
            next_page = "<td><a href=" + self.urls + "?p=%s&content=%s>后一页 &raquo;</a></td>" % (
            self.currentPage + 1, self.content)
        if self.currentPage == self.page_nums:
            prev_page = "<td class='am-disabled'><a href=" + self.urls + "?p=%s&content=%s>&laquo; 前一页</a></td>" % (
            self.currentPage - 1, self.content)
        if self.currentPage == 1:
            next_page = "<td class='am-disabled'><a href=" + self.urls + "?p=%s&content=%s>后一页 &raquo;</a></td>"  % (
            self.currentPage + 1, self.content)

        for page in self.pageRange:
            if page == self.currentPage:
                pageNumStr.append("<td class='center'><span class='label label-important'><a href=" + self.urls + "?p=%s&content=%s>%s</a></span></td>" % (
                page, self.content, page))
            else:
                pageNumStr.append(
                    "<td><span class='label label-important'><a href=" + self.urls + "?p=%s&content=%s>%s</a></span></td>" % (page, self.content, page))
            # print(pageNumStr)

        return prev_page + "".join(pageNumStr) + next_page