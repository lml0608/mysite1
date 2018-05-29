from django.shortcuts import render,HttpResponse,render_to_response,redirect
from django.http import HttpResponse,HttpRequest
from django.template import RequestContext

import datetime

# Create your views here.



def index(request):

    content = {'time':datetime.datetime.now()}

    return render(request,'blog/index.html',content)

def article_year_month(request,year, month):

    #content = {'year':y, 'month':m}

    return HttpResponse("year:%s month:%s"%(year,month))



def article_year_month_day(request,year,month,day):
    #content = {'year':year, 'month':month,'day':day}

    return HttpResponse("year:%s month:%s day:%s"%(year,month,day))



def register(request):


    print(request.path) #/blog/register/

    print(request.get_full_path())  #/blog/register/?uname=liubin&age=28&hobby=1&hobby=2


    print(request.GET)


    if request.method == 'POST':
        print(request.POST) #{'csrfmiddlewaretoken': ['HM2NkUXe4ANk23Zt0UlhZTm07NEcgI3Z7kdudWHCwWRHbXwTsfhayxsaYBH2fiFs'],
        #  'uname': ['343'], 'age': ['3545'], 'hobby': ['3']}>
    return render_to_response('blog/register.html')




