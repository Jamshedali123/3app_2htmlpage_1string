app_name='something'
from django.urls import path
from app1.views import *

urlpatterns=[
    path('newpage1/',newpage1,name='newpage1'),
    path('newpage2/',newpage2,name='newpage2'),
]