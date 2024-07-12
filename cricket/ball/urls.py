from django.urls import path
from ball import views

urlpatterns = [
    path('add/', views.add),
]
