from django.db import models
from trainee.models import *
# Create your models here.
class course(models.Model):
    code=models.CharField(primary_key=True,max_length=10)
    total=models.IntegerField();

class courepertrainee(models.Model):
    ctrainee=models.ManyToManyField(trainee)
    cr=models.ManyToManyField(course);