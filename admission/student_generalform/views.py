from django.shortcuts import render
from student_generalform import forms
from django.http import HttpResponse


# Create your views here.
def add(request):
    if(request.method=='GET'):
        student_form = forms.student_Form()
        data={}
        data['form']=student_form
        return render(request,'student/add.html',context=data)
    else:
        student_data=forms.student_Form(request.POST)
        if(student_data.is_valid()):
            student_data.save(commit=True)
            return HttpResponse("student_generalform\ is added check your table")
