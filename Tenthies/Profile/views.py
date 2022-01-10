from django.contrib.auth.models import User
from django.shortcuts import render
from User.views import deco_auth
from Quiz.models import QuizResult
from Quiz.views import calculate_per
from Profile import models
@deco_auth
def Profile(request):
    #transfer(request)
    user=request.user
    result=QuizResult.objects.filter(user=request.user)
    profile=models.Profile.objects.get(user=request.user)
    print(profile.best_subject)
    total=get_total(result)
    res = render(request,'Profile/profile.html',{'user':user,'result':result,'tresult':total,'total_test':len(result),'profile':profile})
    return res

def get_total(result):
    tres=QuizResult()
    tres.marksobtained=0
    tres.totalmarks=0
    for res in result:
        tres.marksobtained+=int(res.marksobtained)
        tres.totalmarks+=int(res.totalmarks)
    tres.percentage=calculate_per(tres.totalmarks,tres.marksobtained)
    if(tres.percentage!=None):
        tres.percentage=format(tres.percentage,".2f")
    else:
        tres.percentage=float(0)
    return tres

"""
def transfer(request):
    for u in User.objects.all():
        profile=models.Profile()
        profile=subject_details(QuizResult.objects.filter(user=request.user),profile)
        profile.user=u
        profile.save()

def subject_details(result,profile):

    if(len(result)==0):
        profile.weak_subject="None"
        profile.best_subject="None"
        profile.weak_subject_marks=1000
        profile.best_subject_marks=0

        return profile
    
    i=0 
    profile.weak_subject=result[0].subname
    profile.best_subject=result[0].subname
    
    profile.weak_subject_marks=result[0].marksobtained
    profile.best_subject_marks=result[0].marksobtained

    while(i<len(result)-1):
        if(result[i].marksobtained<result[i+1].marksobtained):
            profile.best_subject=result[i+1].subname
            profile.best_subject_marks=result[i+1].marksobtained
        
        elif(result[i].marksobtained>result[i+1].marksobtained):
            profile.weak_subject=result[i+1].subname
            profile.weak_subject_marks=result[i+1].marksobtained
        i+=1
    return profile
"""