from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_car(request):
   
    return render(request,'car/index.html')

def add_car(request):
    return render(request,"car/index1.html")

def update_car(request):
    return render(request,"car/index2.html")
