from django.shortcuts import render

def Home(request):
    res = render(request,'Home/index.html')
    return res