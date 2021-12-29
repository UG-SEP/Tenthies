from os import name
from django.urls import path
from Home.views import Construction, Home,ContactUs, Privacy,Team, Terms,Report

urlpatterns = [
    path('',Home,name='home'),
    path('contact-us',ContactUs,name='contact-us'),
    path('under-contruction',Construction,name='construction'),
    path('team',Team,name="team"),
    path('terms',Terms,name="terms"),
    path('privacy',Privacy,name="privacy"),
    path('report',Report,name="report"),
]