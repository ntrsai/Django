from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show_product(request):
    #messages="<h1>meesho product</h1>"
    #return HttpResponse(messages)
    product_data={'name':'tshirt','price':690}
    return render(request,'product/index.html',context=product_data)