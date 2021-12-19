from django.urls import path
from Quickmap.views import QuickMap

urlpatterns = [
    path('',QuickMap),
]