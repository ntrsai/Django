from veg import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('veg',views.show_veg),
    path('update-veg',views.update_veg),
]
