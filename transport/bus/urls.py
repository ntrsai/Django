from django.urls import path
from bus import views 
urlpatterns = [
    path('bus/', views.show_bus),
    path('add-bus',views.add_bus),
    path('update-bus',views.update_bus)
]
