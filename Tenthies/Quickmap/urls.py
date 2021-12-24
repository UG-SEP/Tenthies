from django.urls import path
from Quickmap.views import QuickMap,SubjectQuickMap

urlpatterns = [
    path('',QuickMap),
    path('subject-quickmap',SubjectQuickMap),
]