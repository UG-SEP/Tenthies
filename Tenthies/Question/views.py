from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from Profile.models import Profile

from Question.models import Comment, UserQuestion
from User.views import deco_auth

# Create your views here.

@deco_auth
def Questions(request):
    all_question=UserQuestion.objects.all()
    return render(request,'Question/All-Questions.html',{'questions':all_question})

@deco_auth
def AddQuestion(request):
    if request.method == "POST":
        description=request.POST.get('description')
        question=request.POST.get('question')
        Userques=UserQuestion()
        Userques.description=description
        Userques.question=question
        Userques.profile=Profile.objects.get(user=request.user)
        Userques.save()
        return redirect('all_question')

    return render(request,'Question/Add-Question.html')

def ViewQuestion(request):
    id=request.GET.get('id')
    question=UserQuestion.objects.get(id=id)
    comments=Comment.objects.filter(userQuestion=question)
    return render(request,'Question/View-Question.html',{'userQues':question,'comments':comments})

def EditQuestion(request):
    if request.method == "POST":
        id=request.GET.get('id')
        userQues=UserQuestion.objects.get(id=id)
        userQues.question=request.POST.get('question')
        userQues.description=request.POST.get('description')
        userQues.save()
        return redirect('all_question')
    
    id=request.GET.get('id')
    userQues=UserQuestion.objects.get(id=id)
    return render(request,'Question/Edit-Question.html',{'userQues':userQues})

def AddAnswer(request):
    id=request.GET.get('id')
    userQues=UserQuestion.objects.get(id=id)
    comment=Comment()
    comment.comment=request.POST.get('comment')
    comment.userQuestion=userQues
    comment.profile=Profile.objects.get(user=request.user)
    comment.save()
    return HttpResponseRedirect('http://localhost:8000/Question/View-Question?id='+str(id))

def Upvote_Question(request):
    id=request.GET.get('id')
    userQues=UserQuestion.objects.get(id=id)
    userQues.like+=1
    userQues.save()
    print(userQues.like)
    return HttpResponseRedirect('http://localhost:8000/Question/View-Question?id='+str(id))
def Devote_Question(request):
    id=request.GET.get('id')
    userQues=UserQuestion.objects.get(id=id)
    userQues.dislike+=1
    userQues.save()
    return HttpResponseRedirect('http://localhost:8000/Question/View-Question?id='+str(id))

def Upvote_Comment(request):
    id=request.GET.get('id')
    comment=Comment.objects.get(id=id)
    comment.like+=1
    comment.save()
    return HttpResponseRedirect('http://localhost:8000/Question/View-Question?id='+str(comment.userQuestion.id))

def Devote_Comment(request):
    id=request.GET.get('id')
    comment=Comment.objects.get(id=id)
    comment.dislike+=1
    comment.save()
    return HttpResponseRedirect('http://localhost:8000/Question/View-Question?id='+str(comment.userQuestion.id))
