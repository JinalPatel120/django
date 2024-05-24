from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('',get_home, name='home'),
   
    #path('post-todo/',post_todo , name='post_todo'),
    path('todo/',todoview.as_view())
    
]