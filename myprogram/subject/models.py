from django.db import models

class subject(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    hours=models.IntegerField()
# Create your models here.

class newtrainee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    nationalnum=models.IntegerField()
    sub=models.ForeignKey(subject,on_delete=models.CASCADE)
