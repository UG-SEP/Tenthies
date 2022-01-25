from Profile.models import Profile
from django.shortcuts import render
from Analytics.logics import get_bestSubjects, get_growthRate, get_specific_subjects, get_subject_details, get_subjects, get_weakSubjects, prepare_data
from django.contrib.auth.models import User
from Profile.views import get_total
from Quiz.models import QuizResult
from User.views import deco_auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

@deco_auth
def All_analysis(request):
    data=[0,0]
    all_subjects=[]
    tvalue=0
    all_subjects=get_subjects()
    results=QuizResult.objects.filter(user=request.user)
    each_subject=prepare_data(all_subjects,results,data)
    try:
        tvalue=(data[0]*100)/data[1]
    except ZeroDivisionError:
        pass

    result=QuizResult.objects.filter(user=request.user)
    weak_subjects=list(set(get_weakSubjects(result)))
    best_subjects=list(set(get_bestSubjects(result)))
    if len(weak_subjects) >= 2:
        weak_subjects=weak_subjects[0:2]
    if len(best_subjects) >= 2:
        best_subjects=best_subjects[0:2]
    growth_rate=get_growthRate(result)
    profile=Profile.objects.get(user=request.user)
    res=QuizResult.objects.filter(user=request.user)
    tres=get_total(res)
    return render(request,'Analytics/Analysis.html',{'weak_subjects':weak_subjects,'best_subjects':best_subjects,
    'growth':growth_rate,'profile':profile,'subjects':each_subject,'tvalue':tvalue,'tres':tres,'total_test':len(res)})



@deco_auth
def Compare_User(request):
    if request.method=='POST':
        try:
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
        except ObjectDoesNotExist:
            messages.error(request,'User Does not exist')

    profiles=sort_users()
    return render(request,'Analytics/User-Compare.html',{'status':'False','topper1':profiles[0],'topper2':profiles[1],
    'topper3':profiles[2]})

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


"""

@deco_auth
def Profile_Viewby(request):
    profile=Profile.objects.get(user=request.user)
    seenby=strToList(profile.seenby)
    print(seenby)
    return render(request,'Analytics/Profile-Viewby.html',{'seenby':seenby})

@deco_auth
def Profile_View(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        user=User.objects.get(username=username)
        profile=Profile.objects.get(user=user)
        seenby=strToList(profile.seenby)
        seenby.append(str(request.user))
        profile.seenby = ',@,'.join(seenby)
        result=QuizResult.objects.filter(user=request.user)
        total=get_total(result)
        profile.save()
        return render(request,'Analytics/View-Profile.html',{'user':user,'result':result,'tresult':total,'total_test':len(result),'profile':profile,'status':'True'})
    
    return render(request,'Analytics/View-Profile.html',{'status':'False'})

"""

def sort_users():
    profile=Profile.objects.all()
    return sorted(profile,key = lambda profile:profile.points,reverse=True)
    