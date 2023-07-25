from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def newpage1(request):
    return render(request,'newpage1.html')

def newpage2(request):
    return render(request,'newpage2.html')

def jamshed1(request):
    return HttpResponse('<h1><marquee>i did my graduation in 2021 from mechanical<marquee></h1>')
