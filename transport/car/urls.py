from django.urls import path
from car import views 
urlpatterns = [
    path('car/', views.show_car),
    path('add-car',views.add_car),
    path('update-car',views.update_car)
]
