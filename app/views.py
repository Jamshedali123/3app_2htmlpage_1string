from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index1(request):
    return render(request,'index1.html')

def index2(request):
    return render(request,'index2.html')

def jamshed(request):
    return HttpResponse('<h1><marquee>i am jamshed and i am persuing my python full stack course from jspider marathahalli</marquee></h1>')