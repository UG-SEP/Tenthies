from django.urls import path
from Profile.views import Profile
urlpatterns = [
    path('',Profile),
]