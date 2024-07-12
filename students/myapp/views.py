from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def insertpage(request):
    return render(request,'myapp/insert.html') 

def insertdata(request):
    if request.method=='POST':
        fname=request.POST['fname']  
        lname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']  

    newuser = Student.objects.create( Firstname=fname,Lastname=lname,Email=email,Contact=contact)
    
    return redirect('show')

def showdata(request):
    all_data=Student.objects.all()
    return render(request,'myapp/show.html',{'key1':all_data})

def update(request,pk):
    update_date=Student.objects.get(id=pk)
    return render(request,'myapp/update.html',{'key2':update_date})
