from django.db import models
from Quiz.models import Subject
class Resource(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    subcode=models.IntegerField()
    subname=models.TextField()
    chname=models.CharField(max_length=400)
    pdf=models.FileField(upload_to="pdfs")
    def __str__(self):
        return self.subname+' | '+self.chname+' | resource'