from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns=[
    path('',Home),
    path('resume/',Resume),
    path('contact/',Contact),
    path('send_msg/',Send),
    path('blog/',Blog),
    path('views/<int:pk>',BlogDetail.as_view()),
    path('comment/',Commenting)
]