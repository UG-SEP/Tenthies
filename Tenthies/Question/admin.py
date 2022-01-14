from django.contrib import admin

from Question.models import Comment, UserQuestion

# Register your models here.
admin.site.register(UserQuestion)
admin.site.register(Comment)
