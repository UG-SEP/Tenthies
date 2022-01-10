from django.db import models
from Quiz.models import Subject
class Resource(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    pdf=models.FileField(upload_to="pdfs")
    def __str__(self):
        return self.subject.subname+' | '+self.subject.chname+' | resource'