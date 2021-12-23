from django.contrib import admin

from Quiz.models import Question, QuizResult, Subject

admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(QuizResult)