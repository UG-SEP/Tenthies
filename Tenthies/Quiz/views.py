from django.http.response import HttpResponse
from django.shortcuts import render
from Profile.models import Profile
from Quiz import models
import random
from User.views import deco_auth
from django.contrib import messages
from Quiz.logics import strToList,get_questions,get_correct_answers, getSubjects,get_subjectTest,calculate_per,validate_answers,storeinfo

# global variables which is needed during the Quiz
questions,i,useranswer,subject,result,button=[],0,[],models.Subject(),models.QuizResult,'Next'

@deco_auth
def TakeTest(request):
    # taking questions and i no of question as global one
    global questions,i
    all_questions=models.Question.objects.all()
    questions=getSpecificQuestions(all_questions,request)

    if(len(questions)==0):
        return HttpResponse("<h1 align='center'>Error: No question found</h1><h1 align='center'>Note: We will soon add question in this test</h1>")
    elif(len(questions)!=questions[0].subject.totalquestions and len(questions)<questions[0].subject.totalquestions):
        return HttpResponse("<h1 align='center'>Error: No. of question differs as provided in the subject list")
    random.shuffle(questions)
    res=render(request,'Quiz/show-question.html',{'question':questions[i],'qno':i+1,'totalques':subject.totalquestions})
    return res

@deco_auth
def ShowQues(request):
    # using global variables
    global questions,useranswer,subject,i,result
    if request.GET.get('button') == 'Previous':
        i-=1
        try:
            return render(request,'Quiz/show-question.html',{'question':questions[i],'qno':i+1,'totalques':subject.totalquestions,'userans':useranswer[i]})
        except IndexError:
            return render(request,'Quiz/show-result.html',{'res':result,'zip_data':zip(strToList(result.questions),strToList(result.useranswers),strToList(result.correctanswer))})
    useranswer[i]=request.GET.get('choice')
    try:
        if(i==subject.totalquestions-1):
            correct_answers=validate_answers(useranswer,questions)
            per=calculate_per(subject.totalquestions,correct_answers)
            result=generate_result(correct_answers,subject.totalquestions,per,request)
            result=storeinfo(useranswer,get_questions(questions),result,get_correct_answers(questions))
            reset_quiz()
            result.save()
            res = render(request,'Quiz/show-result.html',{'res':result,'zip_data':zip(strToList(result.questions),strToList(result.useranswers),strToList(result.correctanswer))})
            return res
    except:
        res=render(request,'Quiz/show-result.html',{'res':result,'zip_data':zip(strToList(result.questions),strToList(result.useranswers),strToList(result.correctanswer))})
    i+=1
    try:
        res=render(request,'Quiz/show-question.html',{'question':questions[i],'qno':i+1,'totalques':subject.totalquestions,'userans':useranswer[i]})
    except IndexError:
        res=render(request,'Quiz/show-result.html',{'res':result,'zip_data':zip(strToList(result.questions),strToList(result.useranswers),strToList(result.correctanswer))})
    return res














# Do not touch


def ShowSubjects(request):
    dupsubjects=models.Subject.objects.all()
    subjects=getSubjects(dupsubjects)
    return render(request,'Quiz/show_subjects.html',{'subjects':subjects,'goto':'Quiz/show-test'})


def getSpecificQuestions(all_questions,request):
    specific_questions=[]
    for ques in all_questions:
        if(ques.subject.chname.upper()==request.GET.get('chname').upper() and
        ques.subject.subname.upper()==request.GET.get('subname').upper() and
        ques.subject.level.upper()==request.GET.get('level').upper()):
            specific_questions.append(ques)
            global subject,useranswer
            subject.subcode=request.GET.get('subcode')
            subject.subname=request.GET.get('subname')
            subject.chname=request.GET.get('chname')
            subject.level=request.GET.get('level')
            subject.totalquestions=int(request.GET.get('tques'))
            useranswer = ['']*subject.totalquestions
    return specific_questions

def ShowTest(request):
    subname=request.GET.get('subname')
    sub_test=get_subjectTest(subname)
    messages.warning(request,"More test will be added soon")
    return render(request,'Quiz/show-test.html',{'test_sheet':sub_test,'subname':subname,
    'logo': sub_test[0].logo if len(sub_test)!=0 else ''})

def reset_quiz():
    global questions,i,useranswer,subject
    questions=[]
    i=0
    useranswer=[]
    subject=models.Subject()

def generate_result(correctanswers,totalquestions,percentage,request):
    res=models.QuizResult()
    res.subcode=subject.subcode
    res.subname=subject.subname
    res.chname=subject.chname
    res.level=subject.level
    res.marksobtained=correctanswers
    res.totalmarks=totalquestions
    res.percentage=format(percentage,".2f")
    res.user=request.user
    profile=Profile.objects.get(user=request.user)
    if res.marksobtained>profile.best_subject_marks:
        profile.best_subject_marks=res.marksobtained
        profile.best_subject=res.subname
    elif res.marksobtained<profile.weak_subject_marks:
        profile.weak_subject_marks=res.marksobtained
        profile.weak_subject=res.subname
    
    profile.save()
    
    return res
