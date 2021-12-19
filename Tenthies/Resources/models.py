from django.db import models
import os
from Tenthies.settings import STATIC_DIR
class Resource(models.Model):
    subcode=models.IntegerField()
    subname=models.TextField()
    chname=models.TextField()
    pdf=models.FileField(upload_to=os.path.join(STATIC_DIR,'pdfs'))
    
    def __str__(self):
        return self.subname+' | '+self.chname+' | resource'