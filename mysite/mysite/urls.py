"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from polls import views
from home.views import home

urlpatterns = [
    path('',home),
    path('admin/', admin.site.urls),
    # path('index/',views.index, name='index'),
    # path('<int:question_id>/',views.detail , name='detail'),
    # path('<int:question_id>/results/',views.result , name='result'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('',include('blog.urls')),
    
]

