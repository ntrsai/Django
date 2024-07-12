from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertpage,name='insertpage'),
    path('insert/', views.insertdata,name='insert'),
    path('show/', views.showdata,name='show'),
    path('update/<int:pk>', views.update,name='update'),
]
   