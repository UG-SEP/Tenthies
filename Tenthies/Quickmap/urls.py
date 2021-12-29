from django.urls import path
from Quickmap.views import QuickMap,SubjectQuickMap

urlpatterns = [
    path('',QuickMap,name="quickmap"),
    path('subject-quickmap',SubjectQuickMap),
]