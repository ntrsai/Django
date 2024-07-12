# hospital/urls.py
from django.urls import path
from hospital_management import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('patients/', views.patient_list, name='patient_list'),
    path('appointments/', views.appointment_list, name='appointment_list'),
]

#