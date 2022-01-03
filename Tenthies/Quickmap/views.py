from django.contrib import messages
from django.shortcuts import render
from Quickmap import models
from Quiz.views import getSubjects
from User.views import deco_auth
from Quiz.models import Subject

def SubjectQuickMap(request):
    subname= request.GET.get('subname')
    quickmaps=get_subjectQuickMap(subname)
    if len(quickmaps)==0:
        messages.warning(request,'Quickmap will be added soon')
    res=render(request,'Resources/show-resources.html',{'resources':quickmaps,'subname':subname,'name':'quickmap','logo':quickmaps[0].subject.logo if len(quickmaps)!=0 else ''})
    return res

def QuickMap(request):
    subjects=getSubjects(Subject.objects.all())
    return render(request,'Quiz/show_subjects.html',{'subjects':subjects,'goto':'quickmap/subject-quickmap'})
    
def get_subjectQuickMap(subname):
    quickmap=models.QuickMap.objects.all()
    return [map for map in quickmap if map.subname==subname]
