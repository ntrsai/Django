from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_product(request):
    #messages="<h1> welcome products <h1>"
    #return HttpResponse(messages)
    return render(request,'product/index.html')
