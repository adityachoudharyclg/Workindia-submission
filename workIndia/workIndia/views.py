from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # context={
    #     'obj':obj
    # }
    # return render(request,'homepage.html',context)
    return HttpResponse("Hello world")