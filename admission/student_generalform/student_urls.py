from django.urls import path
from student_generalform import views
urlpatterns = [
    path('add/',views.add),
]