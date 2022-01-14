from django.urls import path

from Question.views import Devote_Comment, Devote_Question, EditQuestion, Questions,AddQuestion, Upvote_Comment, Upvote_Question,ViewQuestion,AddAnswer

urlpatterns=[
    path('',Questions,name='all_question'),
    path('Ask-Question',AddQuestion,name="add_question"),
    path('View-Question',ViewQuestion,name="view_question"),
    path('Edit-Question',EditQuestion,name='edit_question'),
    path('Add-Answer',AddAnswer,name='addanswer'),
    path('Upvote-Question',Upvote_Question,name='upvote-question'),
    path('Upvote-Comment',Upvote_Comment,name='upvote-comment'),
    path('Devote-Question',Devote_Question,name='devote-question'),
    path('Devote-Comment',Devote_Comment,name='devote-comment'),
    
]