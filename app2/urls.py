app_name='nothing'
from django.urls import path
from app2.views import *

urlpatterns=[
    path('htmlpage1/',htmlpage1,name='htmlpage1'),
    path('htmlpage2/',htmlpage2,name='htmlpage2'),
]