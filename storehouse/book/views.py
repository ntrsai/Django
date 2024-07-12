from django.shortcuts import render
from book import forms
from django.http import HttpResponse


# Create your views here.
def add(request):
    if(request.method=='GET'):
        book_form = forms.bookstore()
        data={}
        data['form']=book
        return render(request,'book/add.html',context=data)
    else:
        data=forms.book(request.POST)
        if(bookstore.is_valid()):
            bookstore.save(commit=True)
            return HttpResponse("book\ is added check your table")












    return render(request,'book/add.html')
