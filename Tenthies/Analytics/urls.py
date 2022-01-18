from unicodedata import name
from django.urls import path
from Analytics.views import All_analysis,Compare_User,Custom_Subject_Compare
urlpatterns = [

    path('',All_analysis,name="analysis"),
    path('Compare-User',Compare_User,name="compare_with_user"),
    path('Custom-Subject-Compare',Custom_Subject_Compare,name="custom_subject_compare"),
    #path('Profile-Viewby',Profile_Viewby,name="profile_viewby"),
    #path('Profile-View',Profile_View,name="view_profile"),
]