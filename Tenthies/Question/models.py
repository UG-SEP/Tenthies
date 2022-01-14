from django.db import models
from django.db.models.deletion import PROTECT
from Profile.models import Profile

class UserQuestion(models.Model):
    profile=models.ForeignKey(Profile,on_delete=PROTECT)
    question=models.TextField()
    description=models.TextField()
    date_time=models.DateTimeField(auto_now=True)
    like=models.BigIntegerField(default=0)
    dislike=models.BigIntegerField(default=0)
    def __str__(self):
        return self.question

class Comment(models.Model):
    comment=models.TextField()
    userQuestion=models.ForeignKey(UserQuestion,on_delete=PROTECT,null=True)
    profile=models.ForeignKey(Profile,on_delete=PROTECT)
    date_time=models.DateTimeField(auto_now=True)
    like=models.BigIntegerField(default=0)
    dislike=models.BigIntegerField(default=0)
    def __str__(self):
        return self.comment