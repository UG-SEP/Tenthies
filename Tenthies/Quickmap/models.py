from django.db import models
from Tenthies.settings import STATIC_DIR

class QuickMap(models.Model):
    subcode=models.IntegerField()
    subname=models.CharField(max_length=200)
    chname=models.CharField(max_length=80)
    quickmap=models.ImageField(upload_to=STATIC_DIR+'/images')
    def __str__(self):
        return self.subname+' | '+self.chname+' | quickmap'
