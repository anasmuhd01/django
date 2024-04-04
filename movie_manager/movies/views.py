from django.shortcuts import render

# Create your views here.
def create(request):
    if request.POST:
        print(request.POST)
    return render(request,'create.html')


def list(request):
    sample_dic = {'movies':[{
        
        'description':'this is sample',
        'year':'2001',
        'success':False,
        'img':'one.jpg'
        },
        {
        'title':'two',
        'description':'this is sample',
        'year':'2001',
        'success':False,
        'img':'two.jpg'
        },
        {
        'title':'three',
        'description':'this is sample',
        'year':'2001',
        'success':True,
        'img':'three.jpg'
        },
        {
        'title':'four',
        'description':'this is sample',
        'year':'2001',
        'success':False,
        'img':'four.jpg'
        },
        {
        'title':'five',
        'description':'this is sample',
        'year':'2001',
        'success':True,
        'img':'five.jpg'
        },]}
    return render(request,'list.html',sample_dic)


def edit(request):
    return render(request,'edit.html')