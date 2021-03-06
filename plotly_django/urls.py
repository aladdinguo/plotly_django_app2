"""plotly_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.views.generic import TemplateView
from django.contrib import admin
from plotlydjangoapp import views
from plotlydjangoapp.ccbdata import current_datetime_locals
from ccbjdz.views import CcbjdzListview,ccbjdzListchoice,seleIssue
from ccbjdz import datacleans
from books.views import display_meta, search_form, search, contact, signin, logout_view, upload_file
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^charts', views.charts),
    url(r'^index', views.index,name='index'),
    url(r'^bookings', views.bookings),
    url(r'^calendar', views.calendar),
    url(r'^documentation', views.documentation),
    url(r'^file_managers', views.file_managers),
    url(r'^finances', views.finances),
    url(r'^form_demo', views.form_demo),
    url(r'^form_elements', views.form_elements),
    url(r'^form_validator', views.form_validator),
    url(r'^gallery', views.gallery),
    url(r'^pages', views.pages),
    url(r'^product_edit', views.product_edit),
    url(r'^tables', views.tables),
    url(r'^jls1',views.jls1),
    url(r'^selcet_item',seleIssue,name='selcet_item'), #选择列表，统计所有数据列出来，然后分类选择。
    url(r'^dataclean',datacleans.readdataworksheet,name='dataclean'), #数据清理，把数据库里的文字后面多余的重复字符去掉。
    url(r'^ui', views.ui),
    url(r'^datain', views.datain),
    url(r'^uploadFile$', upload_file, name='uploadFile'),
    url(r'^hello$', display_meta),
    url(r'^search_form$', search_form),
    url(r'^search$', search),
    url(r'^contact$', contact),
    url(r'^current_date_time$', views.current_date_time),
    url(r'^current_datetime_locals', current_datetime_locals),
    url(r'^6Dchart', views.Dcharts),
    url(r'^loginuser/$', signin),
    url(r'^logoutuser$', logout_view, name='logout_view'),
    url(r'^start$', views.start, name='start'),
    url(r'^ccbdata',views.current_date_time),
    url(r'^detail_list',ccbjdzListchoice.as_view()),
    url(r'^$', views.login1, name='do_login'),
]
