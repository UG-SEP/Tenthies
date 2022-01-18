from django.shortcuts import redirect, render
from Quiz.logics import strToList
from User.views import deco_auth
from Quiz.models import QuizResult
from Quiz.logics import calculate_per
from Profile import models
from django.contrib.auth.models import User
@deco_auth
def Profile(request):
    #transfer(request)
    #add()
    user=request.user
    result=QuizResult.objects.filter(user=request.user)
    profile=models.Profile.objects.get(user=request.user)
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

def Show_details(request):
    status = True
    correctanswer=request.GET.get('correctanswer')
    questions=request.GET.get('questions')
    useranswer=request.GET.get('useranswers')
    if len(questions)==0:
        status=False
    return render(request,'Profile/Quiz-history-details.html',{'zip_data':zip(strToList(questions),strToList(useranswer),strToList(correctanswer)),'status':status})

def ChangePhoto(request):
    if(len(request.FILES)!=0):
        profile=models.Profile.objects.get(user=request.user)
        profile.profile_img=request.FILES['image']
        profile.save()
    
    return redirect('profile')

"""
def add():
    users=User.objects.all()
    for user in users:
        res=QuizResult.objects.filter(user=user)
        profile=models.Profile.objects.get(user=user)
        profile.points=get_points(res)
        profile.save()

def get_points(results):
    points=0
    for res in results:
        if res.marksobtained/(res.totalmarks/10) <= 5 and res.marksobtained/(res.totalmarks/10) > 3:
            points+=1
        elif res.marksobtained/(res.totalmarks/10) <= 9 and res.marksobtained/(res.totalmarks/10) > 5:
            points+=2
        elif res.marksobtained/(res.totalmarks/10) == 10:
            points+=3
        else:
            pass
    return points
"""