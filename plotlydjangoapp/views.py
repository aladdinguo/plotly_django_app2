import os
from django.shortcuts import redirect, render, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from plotlydjangoapp.equipment_info import equi

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
# Create your views here.
from plotlydjangoapp.chart_plot import ChartPlot
from plotlydjangoapp.ccbdata import ccb_data

ccb = ccb_data()
chart = ChartPlot()
context = {}


@login_required(login_url='do_login')
def index(request):
    context['graph_range_slide'] = chart.range_slide()
    context.update({'username': request.user.username})
    context.update({'equi_list': equi.get_queryset})
    return render(request, 'index.html', context=context)


@login_required(login_url='do_login')
def start(request):
    return render(request, 'index.html', {'username': request.user.username})


@login_required(login_url='do_login')
def charts(request):
    context['graph_basic_plot'] = chart.basic_plot()
    context['graph_line_full'] = chart.line_full()
    context['graph_bar_chart'] = chart.bar_chart()
    context['graph_bonus_chart'] = chart.bonus_chart()
    context['graph_pie_chart'] = chart.pie_chart()
    context['graph_stacked_bar'] = chart.stacked_bar()
    context['graph_horizontal_chart'] = chart.horizontal_chart()
    # context['graph_four_chart'] = chart.four_char()
    return render(request, 'charts.html', context=context)


@login_required(login_url='do_login')
def Dcharts(request):
    context['graph_four_chart'] = chart.four_char()
    return render(request, '6Dchart.html', context=context)


@login_required(login_url='do_login')
def finances(request):
    return render(request, 'finances.html')


@login_required(login_url='do_login')
def ui(request):
    return render(request, 'ui.html')


@login_required(login_url='do_login')
def tables(request):
    return render(request, 'tables.html')


@login_required(login_url='do_login')
def form_demo(request):
    return render(request, 'form_demo.html')


@login_required(login_url='do_login')
def form_elements(request):
    return render(request, 'form_elements.html')


@login_required(login_url='do_login')
def bookings(request):
    return render(request, 'bookings.html')


@login_required(login_url='do_login')
def calendar(request):
    return render(request, 'calendar.html')


@login_required(login_url='do_login')
def documentation(request):
    return render(request, 'documentation.html')


@login_required(login_url='do_login')
def file_managers(request):
    return render(request, 'file_managers.html')


@login_required(login_url='do_login')
def form_elements(request):
    return render(request, 'form_elements.html')


@login_required(login_url='do_login')
def form_validator(request):
    return render(request, 'form_validator.html')


@login_required(login_url='do_login')
def gallery(request):
    return render(request, 'gallery.html')


def login1(request):
    return render(request, 'login.html')


@login_required(login_url='do_login')
def pages(request):
    return render(request, 'pages.html')


@login_required(login_url='do_login')
def product_edit(request):
    return render(request, 'product_edit.html')


@login_required(login_url='do_login')
def current_date_time(request):
    context['current_date'] = ccb.current_date()
    return render(request, 'ccbdata.html', context=context)


@login_required(login_url='do_login')
def datain(request):
    return render(request, 'datain.html')


@login_required(login_url='do_login')
def jls1(request):
    return render(request, 'jls1.html')
