from django.urls import path
from product import views

urlpatterns = [
    path('product/',views.show_product),

]

