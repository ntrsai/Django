from django.shortcuts import render
from django.http import HttpReponse
# Create your views here.
def show_veg(request):
    messages="welcome veg</h1>"
    return HttpReponse(messages)
    veg_data={'name':'biryani','price':200}
    return render(request,'veg/index.html',context=veg_data)

def update_veg(request):
    messages="<h1>update veg</h1>"
    return HttpReponse(messages)    
