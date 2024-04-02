from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first_one(request):
    return HttpResponse('helo django')

def second_one(requset):
    return HttpResponse('second')
