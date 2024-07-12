from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_user(request):
    #messages="<h1>meesho user</h1>"
    #return HttpResponse(messages)
    user_data={'name':'ntrsai','age':21}
    return render(request,'user/index.html',context=user_data)