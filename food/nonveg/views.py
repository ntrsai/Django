from django.shortcuts import render
from django.http import HttpReponse


# Create your views here.
def show_nonveg(request):
    #messages="welcome nonveg</h1>"
    #return HttpReponse(messages)
    nonveg_data={'name':'chicken','price':200}
    return render(request,'nonveg/index.html',context=nonveg_data)
def update_nonveg(request):
    messages="<h1>update nonveg</h1>"
    return HttpReponse(messages)    
    
