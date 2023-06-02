from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=Teams.objects.all()
    return render(request,'index.html',{'result':obj,'res':obj2})
    # name='india'
    # return render(request,'home.html',{'obj':name})
# def about(request):
#     return render(request,'abouts.html')
# def contact(request):
#     return HttpResponse('am contact page')
# def addition(request):
#     a=int(request.GET['num1'])
#     b=int(request.GET['num2'])
#     res=a+b
#     return render(request,'abouts.html',{'result':res})
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
def news(request):
    return render(request,'news.html')
def elements(request):
    return render(request,'elements.html')
def destination(request):
    return render(request,'destination.html')


