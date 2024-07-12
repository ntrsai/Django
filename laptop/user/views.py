from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_user(request):
    #messages="<h1> welcome user<h1>"
    #return HttpResponse(messages)
    return render(request,'user/index.html')