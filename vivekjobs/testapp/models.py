from django.db import models

# Create your models here.
class hydjobs(models.Model):
    date=models.DateField()
    company = models.CharField(max_length=70)
    title = models.CharField(max_length=60)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class knrjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=70)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class ngpjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=70)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()


