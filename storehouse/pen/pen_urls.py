from django.urls import path
from pen import views
urlpatterns = [
    path('add/',views.add),
]