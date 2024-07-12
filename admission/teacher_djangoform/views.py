from django.shortcuts import render
from django.http import HttpResponse
from teacher_djangoform.forms import TeacherForm
from teacher_djangoform.models import Teacher


# Create your views here.
def add(request):
    teacher_form = TeacherForm()
    data={}
    data['form']=teacher_form
    if(request.method=='POST'):
        teacherformdata=TeacherForm(request.POST)
        teacher=Teacher()
        if(teacherformdata.is_valid()):
            teacher.name=teacherformdata.cleaned_data['name']
            teacher.phone=teacherformdata.cleaned_data['phone']
            teacher.salary =teacherformdata.cleaned_data['city']
            print(teacher.name,teacher.phone,teacher.city)
            teacher.save()
            return HttpResponse('teacher added ,please check your database')
    return render(request,'teacher/add.html',context=data)
