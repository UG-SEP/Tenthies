from django.contrib.admin.helpers import checkbox
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Quiz import models
import random

from User.views import deco_auth
questions=[]
i=0
useranswer=[]
subject=models.Subject()
def ShowSubjects(request):
    subjects=models.Subject.objects.all()
    res=render(request,'Quiz/show_subjects.html',{'subjects':subjects})
    return res

@deco_auth
def TakeTest(request):
    global questions,i
    all_questions=models.Question.objects.all()
    questions=getSpecificQuestions(all_questions,request)
    if(len(questions)==0):
        return HttpResponse("<h1>Error No question found</h1>")
    random.shuffle(questions)
    i+=1
    res=render(request,'Quiz/show-question.html',{'question':questions[i-1],'qno':i})
    return res

@deco_auth
def ShowQues(request):
    global questions,i
    useranswer.append(request.POST.getlist('choice'))
    if(i==10):
        correct_answers=validate_answers(useranswer,questions)
        per=calculate_per(10,correct_answers)
        result=generate_result(correct_answers,10,per,request)
        result.save()
        res = render(request,'Quiz/show-result.html',{'res':result})
        return res
    i+=1
    res=render(request,'Quiz/show-question.html',{'question':questions[i-1],'qno':i})
    return res

def getSpecificQuestions(all_questions,request):
    specific_questions=[]
    for ques in all_questions:
        if(ques.chname.upper()==request.GET.get('chname').upper() and
        ques.subname.upper()==request.GET.get('subname').upper() and
        ques.level.upper()==request.GET.get('level').upper()):
            specific_questions.append(ques)
            global subject
            subject.subcode=request.GET.get('subcode')
            subject.subname=request.GET.get('subname')
            subject.chname=request.GET.get('chname')
            subject.level=request.GET.get('level')
    return specific_questions

def validate_answers(useranswer,questions):
    correct_answers=0
    i=0
    while(i<len(useranswer)):
        if (str(useranswer[i])) == "['"+(questions[i].answer)+"']":
            correct_answers+=1
        i+=1
    return correct_answers

def calculate_per(totalquestions,correctanswer):
    return (correctanswer*100)/totalquestions

def generate_result(correctanswers,totalquestions,percentage,request):
    res=models.QuizResult()
    res.subcode=subject.subcode
    res.subname=subject.subname
    res.chname=subject.chname
    res.level=subject.level
    res.marksobtained=correctanswers
    res.totalmarks=totalquestions
    res.percentage=percentage
    res.user=request.user
    return res

