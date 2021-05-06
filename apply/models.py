from django.db import models

# Create your models here.
class Apply(models.Model):
    name=models.CharField(max_length=100)
    age=models.TextField()
    text=models.CharField(max_length=500)
    gender=models.BooleanField(default=True)
    pub_date=models.DateTimeField('date published')