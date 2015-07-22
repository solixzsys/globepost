from django.shortcuts import redirect, render
from django.http import response, HttpResponse
from newsapp.models import *
import jsonpickle
from django.core import serializers
def home(request):
    return render(request,'index.html',{})

def test(request):
    return render(request,'index1.html',{})
def test1(request):
    return render(request,'test1.html',{})
def test2(request):
    return render(request,'test2.html',{})
def ajax1(request):
    p=Post.objects.all().order_by("-pub_date")
    #print(p.count())
    data=serializers.serialize("json",p)
   






    return HttpResponse(data,{"content-type":"json"})
