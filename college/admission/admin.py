from django.contrib import admin
from admission import models

# Register your models here.
class studentsAdmin(admin.ModelAdmin):
    list_display=['id','name','date']
admin.site.register(models.students,studentsAdmin)
