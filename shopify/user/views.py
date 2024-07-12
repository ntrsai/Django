from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
   return render(request,'user/home.html')

def register(request):
   data={}
   is_staff=False
   if(request.method=="POST"):
      uname=request.POST['username']
      upass=request.POST['password']
      ucpass=request.POST['cpassword']
      type=request.POST['type']
      if(type=='seller'):
         is_staff=True
      if(uname=="" or upass=="" or ucpass==""):
         data['error_msg']="fields cant be empty"
         return render(request,'user/register.html',context=data)
      elif(upass!=ucpass):
         data['error_msg']="password doen not matched"
         return render(request,'user/register.html',context=data)
      #from django.contrib.auth.models import User
      elif(User.objects.filter(username=uname).exists()):
         data['error_msg']=uname + " is already exist"
         return render(request,'user/register.html',context=data)
      else:
         user=User.objects.create(username=uname,is_staff=is_staff)
         user.set_password(upass)
         user.save()
         return redirect('/login')
   return render(request,'user/register.html',context=data)


def user_login(request):
   data={}
   if(request.method=="POST"):
      uname=request.POST['username']
      upass=request.POST['password']
      if(uname=="" or upass==""):
         data['error_msg']="fields cant be empty"
         return render(request,'user/login.html',context=data)
      elif(not User.objects.filter(username=uname).exists()):
         data['error_msg']=uname + " is does not exist"
         return render(request,'user/login.html',context=data)
      else:
         #from django.contrib.auth import authenticate,login,logout
         user=authenticate(username=uname, password=upass)
         if user is None:
            data['error_msg']="Wrong password"
            return render(request,'user/login.html',context=data)
         else:
            login(request,user)
            if(user.is_staff==True):
               return redirect('/dashboard')
               #return HttpResponse("to dashboard")
            else:
               return redirect('/')
   return render(request,'user/login.html')
def user_logout(request):
    logout(request)
    return redirect('/')