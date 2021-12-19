from django.shortcuts import render

from User.views import deco_auth
from Quiz.models import QuizResult
@deco_auth
def Profile(request):
    user=request.user
    result=QuizResult.objects.filter(user=request.user)
    res = render(request,'Profile/profile.html',{'user':user,'result':result})
    return res