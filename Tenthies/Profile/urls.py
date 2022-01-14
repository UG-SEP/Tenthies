from django.urls import path
from Profile.views import ChangePhoto, Profile, Show_details
urlpatterns = [
    path('',Profile,name="profile"),
    path('show-details',Show_details,name="show-details"),
    path('change-photo',ChangePhoto,name="change_photo")
]