from django.urls import path
from bat import views

urlpatterns = [
    path('add/', views.add),
]
