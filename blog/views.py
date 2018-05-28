from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.



def index(request):

    content = {'time':datetime.datetime.now()}

    return render(request,'blog/index.html',content)
