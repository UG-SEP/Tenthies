from Profile.models import Profile
from django.shortcuts import render
from Analytics.logics import get_specific_subjects, get_subject_details, get_subjects, prepare_data
from django.contrib.auth.models import User
from Profile.views import get_total
from Quiz.models import QuizResult
from User.views import deco_auth

@deco_auth
def All_analysis(request):
    return render(request,'Analytics/All-Analysis.html')

@deco_auth
def Each_Subject(request):
    data=[0,0]
    all_subjects=[]
    all_subjects=get_subjects()
    results=QuizResult.objects.filter(user=request.user)
    each_subject=prepare_data(all_subjects,results,data)
    return render(request,"Analytics/Show-Each-Subject.html",{'subjects':each_subject,
    'tvalue':(data[0]*100)/data[1]})

@deco_auth
def Compare_User(request):
    if request.method=='POST':
        username=request.POST.get('username')
        otherUser=User.objects.get(username=username)
        otherUserProfile=Profile.objects.get(user=otherUser)
        otherUserQuizResults=QuizResult.objects.filter(user=otherUser)
        UserQuizResult=QuizResult.objects.filter(user=request.user)
        UserProfile=Profile.objects.get(user=request.user)
        otherUserPerformance=get_total(otherUserQuizResults)
        yourPerformance=get_total(UserQuizResult)
        return render(request,'Analytics/User-Compare.html',{'otherUserProfile':otherUserProfile,'yourProfile':UserProfile
        ,'otherUserPerformance':otherUserPerformance,'yourPerformance':yourPerformance,'status':'True',
        'yourTest':len(UserQuizResult),'otherTest':len(otherUserQuizResults)})
    
    return render(request,'Analytics/User-Compare.html',{'status':'False'})

@deco_auth
def Custom_Subject_Compare(request):
    if request.method=='POST':
        subject1=request.POST.get('Fsubject')
        subject2=request.POST.get('Ssubject')
        QuizResultsub1=QuizResult.objects.filter(user=request.user)
        QuizResultsub1=get_specific_subjects(subject1,QuizResultsub1)
        QuizResultsub2=QuizResult.objects.filter(user=request.user)
        QuizResultsub2=get_specific_subjects(subject2,QuizResultsub2)
        subDetail1=get_subject_details(QuizResultsub1)
        subDetail2=get_subject_details(QuizResultsub2)
        return render(request,'Analytics/Custom-Subject-Compare.html',{'status':'True','subDetail1':subDetail1,
        'subDetail2':subDetail2,'sub1':subject1,'sub2':subject2})
    return render(request,'Analytics/Custom-Subject-Compare.html',{'status':'False','subjects':get_subjects()})