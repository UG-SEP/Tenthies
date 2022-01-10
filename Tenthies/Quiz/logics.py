from Quiz.models import Subject

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
