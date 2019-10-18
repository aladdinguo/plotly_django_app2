from django.http import HttpResponse
from django.shortcuts import render_to_response, render, reverse, redirect, loader
from books.models import Book
from books.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
import os
from plotly_django import settings
import pandas as pd
import numpy as np



# Create your views here.
def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search_form(request):
    return render_to_response('base.html')


def search(request):
    error = []
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            error.append('输入一个查询term')
        elif len(q) > 10:
            error.append('请输入一个20位字符以内的term')
            return render_to_response('base.html', {'error': error})
        else:
            books = Book.objects.filter(title__icontains=q)
            if books:
                return render_to_response('base.html',
                                          {'books': books, 'query': q})
            else:
                error.append('数据库里没有你想要的数据')
                return render_to_response('base.html', {'query': q, 'error': error})
    else:
        error.append('请输入一个有效内容')
        return render_to_response('base.html', {'error': error})


# def contact(request):
#     errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject', ''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message', ''):
#             errors.append('Enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid e‐mail address.')
#         if not errors:
#             send_mail(
#                 request.POST['subject'],
#                 request.POST['message'],
#                 request.POST.get('email', 'noreply@example.com'),
#                 ['siteowner@example.com'],
#             )
#             return HttpResponseRedirect('/current_date_time/')
#     return render_to_response('base.html',
#                               {'errors': errors,
#                               'subject':request.POST.get('subject',''),
#                                'message':request.POST.get('message',''),
#                                'email':request.POST.get('email','')})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.changed_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
        return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('base.html', {'form': form})

#验证登录用户数据
def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    username = request.POST.get('name_id', '')
    password = request.POST.get('password_id', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(reverse('index'))
        else:
            return redirect(reverse('do_login'))
    else:
        return redirect(reverse('do_login'))


def logout_view(request):
    logout(request)
    return redirect(reverse('do_login'))


def upload_file_s(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        data_list = []
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return render_to_response('datain.html', {'erros': '没有上传文件！'})
        destination = open(os.path.join(settings.BASE_DIR, 'books/upload', myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        path = settings.BASE_DIR + '/books/upload/' + myFile.name
        if os.path.splitext(path)[1] in ['.csv', '.CSV']:
            df_data = pd.read_csv(path).head()
            data = df_data.values[:, :]
            for line in data:
                print(line, type(line), 'line')
                ls = []
                for j in line:
                    ls.append(j)
                    print(ls, type(ls), 'ls')
                data_list.append(ls)
        elif os.path.splitext(path)[1] in ['xls', 'XLS']:
            df_data = pd.read_excel(path).head()
            data = df_data.values[:, :]
            for line in data:
                ls = []
                for j in line:
                    ls.append(j)
                data_list.append(ls)
        else:
            df_data = '文件格式不对，只能读取csv、xls为扩展名的文件。'
        print(df_data)
        return render(request, 'datain.html', {'success': '文件上传成功🙆‍♂️', 'data_list': data_list, 'df_data': df_data,
                                               'df_list': df_data.to_html(index=False)})


def upload_file(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        data_list = []
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return render_to_response('datain.html', {'erros': '没有上传文件！'})
        destination = open(os.path.join(settings.BASE_DIR, 'books/upload', myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        path = settings.BASE_DIR + '/books/upload/' + myFile.name
        print(os.path.splitext(path)[1])
        if os.path.splitext(path)[1] in ['.csv', '.CSV']:
            df_data = pd.read_csv(path).head()
            df_array = np.array(df_data)
            df_list = df_array.tolist()

        elif os.path.splitext(path)[1] in ['.xls', '.XLS','.xlsx']:
            df_data = pd.read_excel(path).head()
            df_array = np.array(df_data)
            df_list = df_array.tolist()

        else:
            df_list = ''
            df_data = '文件格式不对，只能读取csv、xls为扩展名的文件。'
        return render_to_response('datain.html', {'success': '文件上传成功🙆‍♂️', 'data_list': df_list, 'df_data': df_data})
