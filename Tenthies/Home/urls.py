from django.urls import path
from Home.views import Construction, Home,ContactUs

urlpatterns = [
    path('',Home,name='home'),
    path('contact-us',ContactUs,name='contact-us'),
    path('under-contruction',Construction,name='construction')
]