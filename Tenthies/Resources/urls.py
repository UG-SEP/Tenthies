from django.urls import path
from Resources.views import Resources, SubjectResources
urlpatterns = [
    path('',Resources),
    path('subject-resources',SubjectResources)
]