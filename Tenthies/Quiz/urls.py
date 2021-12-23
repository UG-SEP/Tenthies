from django.urls import path

from Quiz.views import ShowSubjects,TakeTest,ShowQues,ShowTest

urlpatterns=[
    path('',ShowSubjects),
    path('take-test',TakeTest),
    path('show-ques',ShowQues),
    path('show-test',ShowTest),
]