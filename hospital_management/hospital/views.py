# hospital/views.py
from django.shortcuts import render, get_object_or_404
from hospital.models import Doctor, Patient, Appointment

def index(request):
    return render(request, 'hospital/index.html')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospital/doctor_list.html', {'doctors': doctors})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/patient_list.html', {'patients': patients})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'hospital/appointment_list.html', {'appointments': appointments})
