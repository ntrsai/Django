from django.urls import path
from book import views
urlpatterns = [
    path('add/',views.add),
]