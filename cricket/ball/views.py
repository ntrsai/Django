from django.shortcuts import render
from django.http import HttpResponse
from ball import forms

# Create your views here.
def add(request):
    if(request.method=='GET'):
        ball_form=forms.Ball_Form()
        data={}
        data['form']=ball_form
        return render(request,'ball/add.html',context=data)

    else:
      ball_data=forms.Ball_Form(request.POST)
      if(ball_data.is_valid()):
        ball_data.save(commit=True)
        return HttpResponse('done progresss')
        




        