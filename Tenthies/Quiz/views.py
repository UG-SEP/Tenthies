from django.http.response import HttpResponse
from django.shortcuts import render 
from Quiz import models
from User.views import deco_auth
from django.contrib import messages
from Quiz.logics import generate_result, getSpecificQuestions, listToStr, reset_quiz, strToList,get_questions,get_correct_answers, getSubjects,get_subjectTest,calculate_per,validate_answers,storeinfo
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

@deco_auth
def TakeTest(request):
    detail=models.QuizDetails()
    detail.i=0
    detail.user=request.user
    detail.button="Next"
    detail.subject=models.Subject.objects.get(id=request.GET.get('id'))
    detail.useranswer=''
    detail.save()
    all_questions=models.Question.objects.all()
    detail=getSpecificQuestions(all_questions,request,detail)

    if detail.subject.totalquestions>len(detail.questions.all()):
        return HttpResponse('<h1>Error No question found</h1>')

    return render(request,'Quiz/show-question.html',{'qno':detail.i+1,'question':detail.questions.all()[detail.i],
    'totalques':detail.subject.totalquestions,'detail':detail})

@deco_auth
def ShowQues(request):
    id=int(request.GET.get('id'))
    try:
        detail=models.QuizDetails.objects.get(id=id)
    except ObjectDoesNotExist:
        return redirect('quiz')

    if request.GET.get('choice')!=detail.questions.all()[detail.i].option1 and request.GET.get('choice')!=detail.questions.all()[detail.i].option2 and request.GET.get('choice')!=detail.questions.all()[detail.i].option3 and request.GET.get('choice')!=detail.questions.all()[detail.i].option4:
        return render(request,'Quiz/show-question.html',{'qno':detail.i+1,'question':detail.questions.all()[detail.i],
        'totalques':detail.subject.totalquestions,'detail':detail})  

    useranswer=strToList(detail.useranswer)

    if request.GET.get('button') == 'Previous':
        detail.i-=1
        detail.save()
        return render(request,'Quiz/show-question.html',{'question':detail.questions.all()[detail.i],
        'qno':detail.i+1,'totalques':detail.subject.totalquestions,'userans':useranswer[detail.i],
        'detail':detail})
    
    
    if len(useranswer)<=detail.i:
        useranswer.append(request.GET.get('choice'))
    else:
        useranswer[detail.i]=request.GET.get('choice')

    detail.useranswer=listToStr(useranswer)
    detail.i+=1
    detail.save()

    if(detail.i==detail.subject.totalquestions):
            correct_answers=validate_answers(useranswer,detail.questions.all())
            per=calculate_per(detail.subject.totalquestions,correct_answers)
            result=generate_result(correct_answers,per,request,detail)
            detail.result=models.QuizResult()
            result=storeinfo(useranswer,get_questions(detail.questions.all()),result,get_correct_answers(detail.questions.all()))
            reset_quiz(detail)
            result.save()
            detail.result=result
            res = render(request,'Quiz/show-result.html',{'res':result})
            return res
    else:
        return render(request,'Quiz/show-question.html',{'qno':detail.i+1,'question':detail.questions.all()[detail.i],
        'totalques':detail.subject.totalquestions,'detail':detail})


def ShowSubjects(request):
    dupsubjects=models.Subject.objects.all()
    subjects=getSubjects(dupsubjects)
    return render(request,'Quiz/show_subjects.html',{'subjects':subjects,'goto':'Quiz/show-test'})


def ShowTest(request):
    subname=request.GET.get('subname')
    sub_test=get_subjectTest(subname)
    messages.warning(request,"More test will be added soon")
    return render(request,'Quiz/show-test.html',{'test_sheet':sub_test,'subname':subname,
    'logo': sub_test[0].logo if len(sub_test)!=0 else ''})


def Show_details(request):
    result=models.QuizResult.objects.get(id=int(request.GET.get('id')))
    return render(request,'Profile/Quiz-history-details.html',{'zip_data':zip(strToList(result.questions),strToList(result.useranswers),strToList(result.correctanswer)),'status':True})