from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def htmlpage1(request):
    return render(request,'htmlpage1.html')
def htmlpage2(request):
    return render(request,'htmlpage2.html')

def jamshed2(request):
    return HttpResponse('<marquee><h1>i did my graduation from college of engineering roorkee</h1></marquee>')
