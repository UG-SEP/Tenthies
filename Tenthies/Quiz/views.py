from django.http.response import HttpResponse
from django.shortcuts import render
from Quiz import models
import random
from User.views import deco_auth

# global variables which is needed during the Quiz
questions,i,useranswer,subject,result=[],0,[],models.Subject(),models.QuizResult

def ShowSubjects(request):
    dupsubjects=models.Subject.objects.all()
    subjects=getSubjects(dupsubjects)
    return render(request,'Quiz/show_subjects.html',{'subjects':subjects,'goto':'Quiz/show-test'})

@deco_auth
def TakeTest(request):
    # taking questions and i no of question as global one
    global questions,i
    all_questions=models.Question.objects.all()
    questions=getSpecificQuestions(all_questions,request)

    if(len(questions)==0):
        return HttpResponse("<h1 align='center'>Error No question found</h1>")
    random.shuffle(questions)
    res=render(request,'Quiz/show-question.html',{'question':questions[i],'qno':i+1,'totalques':subject.totalquestions})
    return res

@deco_auth
def ShowQues(request):
    # using global variables
    global questions,useranswer,subject,i,result
    useranswer.append(request.GET.getlist('choice'))
    try:
        if(i==subject.totalquestions-1):
            correct_answers=validate_answers(useranswer,questions)
            per=calculate_per(subject.totalquestions,correct_answers)
            result=generate_result(correct_answers,subject.totalquestions,per,request)
            reset_quiz()
            result.save()
            res = render(request,'Quiz/show-result.html',{'res':result})
            return res
    except:
        res=render(request,'Quiz/show-result.html',{'res':result})
    i+=1
    try:
        res=render(request,'Quiz/show-question.html',{'question':questions[i],'qno':i+1,'totalques':subject.totalquestions})
    except IndexError:
        res=render(request,'Quiz/show-result.html',{'res':result})
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
            subject.totalquestions=request.GET.get('tques')
            subject.totalquestions=int(subject.totalquestions)
    return specific_questions

def validate_answers(useranswer,questions):
    correct_answers=0
    i=0
    while(i<len(useranswer)):
        if (str(useranswer[i])) == "['"+(questions[i].answer)+"']":
            print(useranswer[i],questions[i].answer)
            correct_answers+=1
        i+=1
    return correct_answers

def calculate_per(totalquestions,correctanswer):
    try:
        return (correctanswer*100)/totalquestions
    except ZeroDivisionError:
        pass

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
    return res

def reset_quiz():
    global questions,i,useranswer,subject
    questions=[]
    i=0
    useranswer=[]
    subject=models.Subject()

def ShowTest(request):
    subname=request.GET.get('subname')
    sub_test=get_subjectTest(subname)
    return render(request,'Quiz/show-test.html',{'test_sheet':sub_test,'subname':subname,
    'logo': sub_test[0].logo if len(sub_test)!=0 else ''})

def get_subjectTest(subname):
    subjects=models.Subject.objects.all()
    return [sub for sub in subjects if sub.subname==subname]

def getSubjects(dsubjects):
    subjects=[]
    subnames=[]
    for sub in dsubjects:
        if(sub.subname in subnames):
            pass
        else:
            subjects.append(sub)
            subnames.append(sub.subname)
    return subjects