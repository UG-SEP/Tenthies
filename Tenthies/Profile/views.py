from django.shortcuts import render
from User.views import deco_auth
from Quiz.models import QuizResult
from Quiz.views import calculate_per

@deco_auth
def Profile(request):
    user=request.user
    result=QuizResult.objects.filter(user=request.user)
    total=get_total(result)
    res = render(request,'Profile/profile.html',{'user':user,'result':result,'tresult':total,'total_test':len(result)})
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

