from django.db import models

# Create your models here.
class Test(models.Model):
    test=models.CharField(max_length=10)

class Hamshahri(models.Model):
    TYPE=()
    docId=models.CharField(max_length=255)
    date=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    text=models.CharField(max_length=255)