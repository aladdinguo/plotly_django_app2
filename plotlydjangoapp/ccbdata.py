from django.http import HttpResponse,Http404
import datetime
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
class ccb_data:
    def __str__(self):
        pass
    def current_date(self):
        dt=datetime.datetime.now()
        return dt

# def current_datetime(request):
#     now = datetime.datetime.now()
#
#     return render_to_response('current_datetime.html', {'current_date1': now})
def current_datetime_locals(request):
    now = datetime.datetime.now()
    new= datetime.time()
    return render_to_response('current_datetime.html',locals())
