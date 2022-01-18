from django.contrib import admin

from Quiz.models import Question, QuizDetails, QuizResult, Subject

class QuestionAdmin(admin.ModelAdmin):
    search_fields=('ques','subject__subname','subject__level','subject__subcode')
    list_filter=('subject__subname','subject__level')

class SubjectAdmin(admin.ModelAdmin):
    search_fields=('subname','subcode','level')
    list_filter=('subname','level')

class QuizResultAdmin(admin.ModelAdmin):
    search_fields=('subname','subcode','level','totalmarks','marksobtained','chname','percentage','user__username')
    list_filter=('subname','level','chname','user__username')

admin.site.register(Subject,SubjectAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(QuizResult,QuizResultAdmin)
admin.site.register(QuizDetails)