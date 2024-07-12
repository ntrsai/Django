from django.shortcuts import render
from django.http import HttpResponse
from bat import forms


# Create your views here.
def add(request):
    if(request.method=='GET'):
        bat_form=forms.Bat_Form()
        data={}
        data['form']=bat_form
        return render(request,'bat/add.html',context=data)

    else:
        bat_data=forms.Bat_Form(request.POST)
        if(bat_data.is_valid()):
            bat_data.save(commit=True)
            return HttpResponse('DONE PROGRESS')
