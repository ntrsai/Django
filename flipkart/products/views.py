from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def show_products(request):
    #message="<h1>products </h1>"
    #return HttpResponse(message)
    products_data={'name':shirt,'price':201}
    return render(request,'products/index.html',context=products_data)

def update_products(request):
    message="<h1>  hello update products </h1>"
    return HttpResponse(message)

def delete_products(request):
    message="<h1>hello delete products </h1>"
    return HttpResponse(message)


