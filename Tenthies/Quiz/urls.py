from django.urls import path

from Quiz.views import ShowSubjects,TakeTest,ShowQues,ShowTest

urlpatterns=[
    path('',ShowSubjects,name="quiz"),
    path('take-test',TakeTest,name="take_quiz"),
    path('show-ques',ShowQues,name="show_question"),
    path('show-test',ShowTest,name="show_quiz"),
]