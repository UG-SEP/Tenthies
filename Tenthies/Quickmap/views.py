from django.shortcuts import render
from Quickmap import models
from User.views import deco_auth

@deco_auth
def QuickMap(request):
    quickmaps=models.QuickMap.objects.all()
    res=render(request,'QuickMap/show-maps.html',{'quickmaps':quickmaps})
    return res
