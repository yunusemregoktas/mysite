from django.db import models
from urun import *

class Urun(models.Model):
    ad = models.CharField(max_length=200)
    kod = models.CharField(max_length=200)
    marka = models.ForeignKey('marka' , on_delete=models.CASCADE)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.ad

class marka(models.Model):
    ad=models.CharField(max_length=200)

    def __str__(self):
        return self.ad
    