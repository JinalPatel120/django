from django.urls import path,re_path
from django.contrib import admin
from . import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from .views import Home

schema_view = get_schema_view(
    openapi.Info(
        title="Blog ",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
  
    path('', views.post_line, name='post_list'),
    path('post<int:pk>/',views.post_detail,name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', Home.as_view()),  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






