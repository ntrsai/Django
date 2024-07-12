from django.shortcuts import render
from django.http import HttpResponse
from employee_djangoform.forms import EmployeeForm
from employee_djangoform.models import Employee


# Create your views here.
def add(request):
    employee_form = EmployeeForm()
    data={}
    data['form']=employee_form
    if(request.method=='POST'):
        employeeformdata=EmployeeForm(request.POST)
        employee=Employee()
        if(employeeformdata.is_valid()):
            employee.name=employeeformdata.cleaned_data['name']
            employee.phone=employeeformdata.cleaned_data['phone']
            employee.salary =employeeformdata.cleaned_data['salary']
            print(employee.name,employee.phone,employee.salary)
            employee.save()
            return HttpResponse('employee added ,please check your database')
    return render(request,'employee/add.html',context=data)
