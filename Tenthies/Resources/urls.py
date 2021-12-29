from django.urls import path
from Resources.views import Resources, SubjectResources
urlpatterns = [
    path('',Resources,name="resources"),
    path('subject-resources',SubjectResources,name="resources_subject")
]