from nonveg import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nonveg',views.show_nonveg),
    path('update-nonveg',views.update_nonveg),

]
