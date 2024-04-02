from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def first_one(request):
    return HttpResponse('helo django')

def checking_render(req):
    return render(req, "helo.html")
