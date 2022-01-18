from django.contrib.auth.models import User
from django.db import models


class Subject(models.Model):
    logo=models.CharField(max_length=30,default="")
    subcode=models.IntegerField()
    subname=models.CharField(max_length=200)
    level=models.TextField()
    chname=models.CharField(max_length=200)
    totalquestions=models.IntegerField()
    subimg=models.ImageField(upload_to="images")
    sub_bgcolor=models.CharField(max_length=7)
    sub_bgcolor_light=models.CharField(max_length=10)
    sub_textcolor_hover=models.CharField(max_length=10)
    sub_boxshadow_color=models.CharField(max_length=10)

    def __str__(self):
        return self.subname+' | '+self.chname+' | '+self.level

class Question(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,default="")
    ques=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='images',blank=True)
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
    questions=models.TextField(default="")
    useranswers=models.TextField(default="")
    correctanswer=models.TextField(default="")

    def __str__(self):
        return str(self.subcode)+' | '+self.subname+' | '+ self.user.username

class QuizDetails(models.Model):
    questions=models.ManyToManyField(Question,null=True)
    i=models.IntegerField(null=True)
    subject=models.ForeignKey(Subject,on_delete=models.PROTECT,default="")
    button=models.CharField(max_length=40,null=True)
    user=models.ForeignKey(User,on_delete=models.PROTECT,null=True,default="")
    useranswer=models.TextField(default="",null=True)
