from django.shortcuts import render
from datetime import datetime

# Create your views here.
def base(request):
    data={'name': 'raj','age':21,'dob':datetime.now()}
    return render(request,'base.html',context=data)
def politics(request):
    return render(request,'politics/politics.html')
def sports(request):
    return render(request,'sports/sports.html')

def bollywood(request):
    return render(request,'bollywood/bollywood.html')


