from django.urls import path
from Resources.views import ShowResources
urlpatterns = [
    path('',ShowResources),
]