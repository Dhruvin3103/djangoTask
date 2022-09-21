#i have created this
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def home(request,*args,**kwargs):
    return render(request,'home.html',{})


