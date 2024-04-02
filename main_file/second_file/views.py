from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def first_one(request):
    return HttpResponse('helo django')

def checking_render(req):
    sample_dic = {'movies':[{
        
        'description':'this is sample',
        'year':'2001',
        'success':False
        },
        {
        'title':'two',
        'description':'this is sample',
        'year':'2001',
        'success':False
        },
        {
        'title':'three',
        'description':'this is sample',
        'year':'2001',
        'success':True
        },
        {
        'title':'four',
        'description':'this is sample',
        'year':'2001',
        'success':False
        },
        {
        'title':'five',
        'description':'this is sample',
        'year':'2001',
        'success':True
        },]}

    return render(req, "helo.html", sample_dic)
