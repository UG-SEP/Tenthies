from django.urls import path
from Analytics.views import All_analysis,Each_Subject,Compare_User,Custom_Subject_Compare
urlpatterns = [

    path('',All_analysis,name="analysis"),
    path('Each-Subject',Each_Subject,name="each_subject_analysis"),
    path('Compare-User',Compare_User,name="compare_with_user"),
    path('Custom-Subject-Compare',Custom_Subject_Compare,name="custom_subject_compare"),
]