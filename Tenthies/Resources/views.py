from django.db import models
from django.shortcuts import render
from Resources import models
from django.views.decorators.clickjacking import xframe_options_exempt
from Quiz.views import getSubjects
from Quiz.models import Subject

from User.views import deco_auth

@xframe_options_exempt
def SubjectResources(request):
    subname=request.GET.get('subname')
    resources=get_subjectResources(subname)
    print(len(resources))
    res=render(request,'Resources/show-resources.html',{'resources': resources,'subname':subname,'name':'resources'})
    return res

def Resources(request):
    subjects=getSubjects(Subject.objects.all())
    return render(request,'Quiz/show_subjects.html',{'subjects':subjects,'goto':'resources/subject-resources'})
   
def get_subjectResources(subname):
    resources=models.Resource.objects.all()
    return [res for res in resources if res.subname==subname]


