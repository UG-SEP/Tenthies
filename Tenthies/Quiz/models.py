from django.contrib.auth.models import User
from django.db import models

class Subject(models.Model):
    subcode=models.IntegerField()
    subname=models.TextField()
    level=models.TextField()
    chname=models.TextField()
    def __str__(self):
        return self.subname+' | '+self.chname+' | '+self.level

class Question(models.Model):
    subname=models.TextField()
    level=models.TextField()
    chname=models.TextField()
    ques=models.CharField(max_length=1000)
    option1=models.CharField(max_length=400)
    option2=models.CharField(max_length=400)
    option3=models.CharField(max_length=400)
    option4=models.CharField(max_length=400)
    answer=models.CharField(max_length=400,default='None')
    def __str__(self):
        return self.ques

class QuizResult(Subject):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    marksobtained = models.IntegerField()
    totalmarks = models.IntegerField()
    percentage = models.FloatField()
    def __str__(self):
        return str(self.subcode)+' | '+self.subname+' | '+ self.user.username