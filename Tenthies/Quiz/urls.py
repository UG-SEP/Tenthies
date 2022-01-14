from django.urls import path

from Quiz import views

urlpatterns=[
    path('',views.ShowSubjects,name="quiz"),
    path('take-test',views.TakeTest,name="take_quiz"),
    path('show-ques',views.ShowQues,name="show_question"),
    path('show-test',views.ShowTest,name="show_quiz"),
    path('quiz-details',views.Show_details,name="quiz-details"),
]