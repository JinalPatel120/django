from menu.views import *
from django.urls import path

urlpatterns = [
    path('',get_home , name='home')
]
