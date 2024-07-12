from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_user(request):
    #message="<h1>user </h1>"
    #return HttpResponse(message)
    user_date={'name':'sai','age':21}
    return render(request,'user/index.html',context=user_date)

def update_user(request):
    message="<h1> hello update user </h1>"
    return HttpResponse(message)

def delete_user(request):
    message="<h1> hello delete user </h1>"
    return HttpResponse(message)
