from django.shortcuts import render
from django.http import HttpResponse

def show_students(request):
    msg="<h1>wecome students</h1>"
    return HttpResponse(msg)

def update_students(request):
    msg="<h1>wecome update students</h1>"
    return HttpResponse(msg)

def delete_students(request):
    msg="<h1>wecome delete students</h1>"
    return HttpResponse(msg)

