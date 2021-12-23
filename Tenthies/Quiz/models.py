from django.contrib.auth.models import User
from django.db import models
from Tenthies.settings import STATIC_DIR


class Subject(models.Model):
    subcode=models.IntegerField()
    subname=models.CharField(max_length=200)
    level=models.TextField()
    chname=models.CharField(max_length=200)
    totalquestions=models.IntegerField(default=10)
    subimg=models.ImageField(upload_to=STATIC_DIR+'/images',default="")
    sub_bgcolor=models.CharField(max_length=7,default="#000000")
    sub_bgcolor_light=models.CharField(max_length=10,default="#000000")
    sub_textcolor_hover=models.CharField(max_length=10,default="#000000")
    sub_boxshadow_color=models.CharField(max_length=10,default="#000000")

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
    answer=models.CharField(max_length=400)
    def __str__(self):
        return self.ques

class QuizResult(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    marksobtained = models.IntegerField()
    totalmarks = models.IntegerField()
    percentage = models.FloatField()
    subcode=models.IntegerField()
    subname=models.CharField(max_length=200)
    level=models.TextField()
    chname=models.CharField(max_length=200)

    def __str__(self):
        return str(self.subcode)+' | '+self.subname+' | '+ self.user.username