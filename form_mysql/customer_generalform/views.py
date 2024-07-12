from django.shortcuts import render
from customer_generalform import forms
from django.http import HttpResponse


# Create your views here.
def add(request):
    if(request.method=='GET'):
        customer_form = forms.Customer_Form()
        data={}
        data['form']=customer_form
        return render(request,'customer/add.html',context=data)
    else:
        customer_data=forms.Customer_Form(request.POST)
        if(customer_data.is_valid()):
            customer_data.save(commit=True)
            return HttpResponse("customer_generalform\ is added check your table")
