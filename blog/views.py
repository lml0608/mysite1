from django.shortcuts import render,HttpResponse,render_to_response,redirect
from django.http import HttpResponse,HttpRequest
from django.template import RequestContext

from .models import *

import datetime

# Create your views here.


def duobiao(request):


    return render(request,'blog/duobiao.html')



def addbook2(request):

    #

    #publish_obj = Publish.objects.filter(name="人民出版社")[0]

    #book = Book.objects.filter(publish=publish_obj)
    #book = Book.objects.filter(publish__city='北京')
    #
    # Book.objects.create(name='js',pub_date='2017-12-05',price=88,publish=publish_obj)

    #book = Book.objects.get(name="python")

    # print(book)
    # name1 = book.publish.name

    book1 = Publish.objects.filter(name="人民出版社")[0].book_set.all()

    return HttpResponse(book1)


def update2(request):

    rows = Book.objects.filter(name='js').update(price=56)

    if rows>0:
        return HttpResponse('success')

    return HttpResponse("failed")


def delete2(request):
    Book.objects.filter(name='js').delete()

    return HttpResponse('success')

def selectbook2(request):

    #指定查找的字段values()  排序order_by()
    #booklist = Book.objects.all().values('id','name','price').order_by('-id')
    #去重distinct
    #b1 = Book.objects.filter(name='js').values('name','price').distinct()
    #exclude和filter相反
    #b = Book.objects.exclude(name='js').count()

    #b2 = Book.objects.filter(price__gt=50)
    b2 = Book.objects.filter(name__startswith='py')


    #查询单条记录，不是结果集
    #b3 = Book.objects.get(price=50)


    return render(request,'blog/book.html',{'booklist':b2})




def book(request):

    return render(request,'blog/book.html')



def addbook(request):


    Book.objects.create(name='js',pub_date='2017-12-05',price=88,author='smith')

    return HttpResponse('success')


def update(request):

    Book.objects.filter(name='js').update(price=56)

    return HttpResponse('success')


def delete(request):
    Book.objects.filter(name='js').delete()

    return HttpResponse('success')

def selectbook(request):

    #指定查找的字段values()  排序order_by()
    #booklist = Book.objects.all().values('id','name','price').order_by('-id')
    #去重distinct
    #b1 = Book.objects.filter(name='js').values('name','price').distinct()
    #exclude和filter相反
    #b = Book.objects.exclude(name='js').count()

    #b2 = Book.objects.filter(price__gt=50)
    b2 = Book.objects.filter(name__startswith='py')


    #查询单条记录，不是结果集
    #b3 = Book.objects.get(price=50)


    return render(request,'blog/book.html',{'booklist':b2})






def index(request):

    time = datetime.datetime.now()


    test = "hello world!"
    test2 = "h  ell   o wor ld!"
    num = 10

    list1 = []
    list2 = False
    a = "<a href=''>click</a>"

    return render(request,'blog/index.html',locals())

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




