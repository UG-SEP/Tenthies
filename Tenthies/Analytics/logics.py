from Quiz.models import Subject

class SubjectDetails():
    def __init__(self):
        self.total_test=0
        self.total_marks=0
        self.marksobtained=0
        self.best_chapter='None'
        self.weak_chapter='None'
        self.best_chapter_marks=0
        self.weak_chapter_marks=1000
        self.percentage=0.0

def get_subjects():
    subjects=Subject.objects.all()
    return list(set([sub.subname for sub in subjects]))

def prepare_data(all_subjects,results,data):
    subjects={sub:0 for sub in all_subjects}
    times={sub:0 for sub in all_subjects}
    for res in results:
        subjects[res.subname]+=res.marksobtained
        times[res.subname]+=res.totalmarks
        print(subjects,times)
    for subname,value in subjects.items():
        try:
            data[0]+=subjects[subname]
            data[1]+=times[subname]
            subjects[subname]=int((value*100)/(times[subname]))
            print(subjects[subname],times[subname])
        except ZeroDivisionError:
            pass
    return subjects

def get_subject_details(result):
    sub_detail=SubjectDetails()
    if len(result)==0:
        return sub_detail
    sub_detail.best_chapter=result[0].chname
    sub_detail.weak_chapter=result[0].chname
    sub_detail.total_test=len(result)
    for res in result:
        sub_detail.total_marks+=res.totalmarks
        sub_detail.marksobtained+=res.marksobtained

        if sub_detail.best_chapter_marks<res.marksobtained:
            sub_detail.best_chapter_marks=res.marksobtained
            sub_detail.best_chapter=res.chname
        
        if sub_detail.weak_chapter_marks>res.marksobtained:
            sub_detail.weak_chapter_marks=res.marksobtained
            sub_detail.weak_chapter=res.chname
    
    sub_detail.percentage=(sub_detail.marksobtained*100)/sub_detail.total_marks
    sub_detail.percentage=format(sub_detail.percentage,".2f")
    return sub_detail

def get_specific_subjects(subname,result):
    return [res for res in result if res.subname==subname]