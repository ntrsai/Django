from django.shortcuts import render
from django.http import HttpResponse

def show_teachers(request):
    msg="<h1>welcome teachers</h1>"
    return HttpResponse(msg)

def update_teachers(request):
    msg="<h1>welcome update teachers</h1>"
    return HttpResponse(msg)

def delete_teachers(request):
    msg="<h1>welcome delete teachers</h1>"
    return HttpResponse(msg)

 
 

