from django.db import models
from Quiz.models import Subject
from Tenthies.settings import STATIC_DIR

class QuickMap(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    subcode=models.IntegerField()
    subname=models.CharField(max_length=200)
    chname=models.CharField(max_length=80)
    quickmap=models.ImageField(upload_to=STATIC_DIR+'/images')
    def __str__(self):
        return self.subname+' | '+self.chname+' | quickmap'
