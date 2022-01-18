from Profile.models import Profile
from Quiz.models import QuizResult, Subject

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

def get_subjectTest(subname):
    subjects=Subject.objects.all()
    return [sub for sub in subjects if sub.subname==subname]


def validate_answers(useranswer,questions):
    correct_answers=0
    i=0
    while(i<len(useranswer)):
        if (str(useranswer[i])) == (questions[i].answer):
            correct_answers+=1
        i+=1
    return correct_answers

def calculate_per(totalquestions,correctanswer):
    try:
        return (correctanswer*100)/totalquestions
    except ZeroDivisionError:
        pass

def listToStr(l):
    return ',@,'.join(l)
def storeinfo(useranswer,questions,result,correctanswer):
    result.useranswers=',@,'.join(useranswer)
    result.correctanswer=',@,'.join(correctanswer)
    result.questions=',@,'.join(questions)
    return result    


def get_correct_answers(questions):
    return [ques.answer for ques in questions]

def get_questions(questions):
    return [q.ques for q in questions]

def strToList(data):
    return list(data.split(',@,'))

def getSpecificQuestions(all_questions,request,detail):

    subject=Subject.objects.get(id=request.GET.get('id'))
    for ques in all_questions:
        if(ques.subject.chname.upper()==subject.chname.upper() and
        ques.subject.subname.upper()==subject.subname.upper() and
        ques.subject.level.upper()==subject.level.upper()):
            detail.questions.add(ques)

    return detail

def reset_quiz(detail):
    detail.delete()

def generate_result(correctanswers,percentage,request,detail):
    res=QuizResult()
    res.subcode=detail.subject.subcode
    res.subname=detail.subject.subname
    res.chname=detail.subject.chname
    res.level=detail.subject.level
    res.marksobtained=correctanswers
    res.totalmarks=detail.subject.totalquestions
    res.percentage=format(percentage,".2f")
    res.user=request.user
    profile=Profile.objects.get(user=request.user)
    if res.marksobtained>profile.best_subject_marks:
        profile.best_subject_marks=res.marksobtained
        profile.best_subject=res.subname
    if res.marksobtained<profile.weak_subject_marks:
        profile.weak_subject_marks=res.marksobtained
        profile.weak_subject=res.subname

    if res.marksobtained/(res.totalmarks/10) <= 5 and res.marksobtained/(res.totalmarks/10) > 3:
        profile.points+=1
    elif res.marksobtained/(res.totalmarks/10) <= 9 and res.marksobtained/(res.totalmarks/10) > 5:
        profile.points+=2
    elif res.marksobtained/(res.totalmarks/10) == 10:
        profile.points+=3
    else:
        pass

    profile.chname=res.chname
    profile.level=res.level
    
    profile.save()
    
    return res
