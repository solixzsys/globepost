from django.shortcuts import redirect, render
from django.http import response, HttpResponse
from newsapp.models import *
import jsonpickle
from django.core import serializers
def home(request):
    #print("%%%%%%%  ",section)
    return render(request,'index.html',{})


def test(request):
    return render(request,'index1.html',{})
def test1(request):
    return render(request,'test1.html',{})
def test2(request):
    return render(request,'test2.html',{})
def test4(request):
    return render(request,'test4.html',{})
def ajax1(request,section):
    print(section)
    p=""
    if request.is_ajax():
        if section=="africa":
            p=Post.objects.filter(feed_url__country=Country.objects.get(country_name='NIGERIA')).order_by("-pub_date")
        elif section=="america":
            p=Post.objects.filter(feed_url__country=Country.objects.get(country_name='UNITED STATES')).order_by("-pub_date")
        elif section=="europe":
            p=Post.objects.filter(feed_url__country=Country.objects.get(country_name='UNITED KINGDOM')).order_by("-pub_date")
        else:
            p=Post.objects.all().order_by("-pub_date")
    
        data=serializers.serialize("json",p)
        return HttpResponse(data,{"content-type":"json"})
    else:
        return render(request,'index.html',{})