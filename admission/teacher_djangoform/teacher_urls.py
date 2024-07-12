from django.urls import path
from teacher_djangoform import views
urlpatterns = [
    path('add/',views.add),
]