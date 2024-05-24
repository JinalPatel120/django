from django.contrib import admin
from django.urls import path , include
from  . views import *


urlpatterns = [
       
    # path('',get_data , name='get_data'),
    # path('post-data', post_data, name='post_data'),
    # path('update-student/<int:id>/', update_student , name='update_student'),
    # path('delete-student/<id>/', delete_student, name="delete_student"),
    path('get-book',get_book, name='get_book'),
    #path('student/', StudentAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('student-generic/', student_generic.as_view()),
    path('student-generic1/<id>/', student_generic1.as_view())
    
]

