# hospital/admin.py
from django.contrib import admin
from hospital_management.models import Doctor, Patient, Appointment, Prescription

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Prescription)
