from . import views
from django.urls import path

urlpatterns = [
   path('', views.index , name='index'),
   path('index/', views.index, name='index'),
   path('display/', views.display , name='display'),
   path('delete/<id>', views.delete , name='delete'),
   path('update/<id>' , views.update , name='update')

]
  