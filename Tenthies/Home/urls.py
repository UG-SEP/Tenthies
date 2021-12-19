from django.urls import path
from Home.views import Home

urlpatterns = [
    path('',Home),
]