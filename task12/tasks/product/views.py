from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .import task12
from .models import  product
from .forms import productform,rawform
# Create your views here.

def about(request,*args,**kwargs):
    d={
        "Myself" : "dhruvin",
        "Num" : 1234554,
        "list" : [1,2,'how','are'],
        "html":'<h1>Hello dc</h1>'
    }
    return render(request, "home.html",d)

def task2(request, id1,id2):
    l=task12.task(id1,id2)
    print(l)
    return JsonResponse(l,safe=False)

def prod_det(request):
    form = rawform()
    if request.method == "POST":
        form = rawform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)

    co={'form':form}
    return render(request,"det.html",co)
