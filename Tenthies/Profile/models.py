from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User

class Profile(models.Model):
    user=OneToOneField(User,on_delete=models.CASCADE)
    profile_img=models.ImageField(upload_to='profilePic',null=True,default="",blank=True)
    weak_subject=models.CharField(max_length=80)
    best_subject=models.CharField(max_length=80)
    best_subject_marks=models.IntegerField(default=0)
    weak_subject_marks=models.IntegerField(default=1000)
    chname=models.CharField(max_length=200,default="None")
    level=models.CharField(max_length=40,default="None")
    points=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username