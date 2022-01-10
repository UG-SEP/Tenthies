from django.db import models
from Quiz.models import Subject

class QuickMap(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    quickmap=models.ImageField(upload_to='images')
    def __str__(self):
        return self.subject.subname+' | '+self.subject.chname+' | quickmap'
