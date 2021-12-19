from django.db import models
from django.shortcuts import render
from Resources import models
from django.views.decorators.clickjacking import xframe_options_exempt

from User.views import deco_auth

@xframe_options_exempt
@deco_auth
def ShowResources(request):
    resources=models.Resource.objects.all()
    res=render(request,'Resources/show-resources.html',{'resources': resources})
    return res