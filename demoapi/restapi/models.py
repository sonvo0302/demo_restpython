from django.db import models

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=255,blank=False,default='')
    price =models.IntegerField(default=0)
    description = models.CharField(max_length=255, blank=False, default='')
    published = models.BooleanField(default=False)