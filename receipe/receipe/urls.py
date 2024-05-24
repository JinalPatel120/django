"""
URL configuration for receipe project.

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
from django.contrib import admin
from django.urls import path ,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('menu.urls')),
    path('dishes/',views.dishes , name = 'dishes'),
    path('show/',views.show,name='show'),
    path('delete-receipe/<id>/',views.delete_recepie , name='delete_receipe'),
    path('update-receipe/<id>/',views.update_receipe , name='update_receipe'),
    path('login/',views.login_page , name='login_page') ,
    path('register/', views.register_page , name='register_page'),
    path('logout/',views.logout_page, name='logout_page'),
    path('api/docs/', schema_view)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root= settings.MEDIA_ROOT)
    
    
urlpatterns += staticfiles_urlpatterns()