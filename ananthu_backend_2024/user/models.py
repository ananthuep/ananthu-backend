from django.db import models

# Create your models here.

class Registration(models.Model):
    NAME=models.CharField(max_length=50)
    AGE=models.IntegerField()
    CONTACT=models.CharField(max_length=50)
    PASSWORD=models.CharField(max_length=250)
    USERNAME=models.CharField(max_length=150)
    CATEGORY=models.CharField(max_length=50)
    

class docters(models.Model):
     NAME=models.CharField(max_length=50)
     AGE=models.CharField(max_length=50)
     DATE_OF_BIRTH=models.CharField(max_length=50,null=True,blank=True)
     CONTACT=models.CharField(max_length=12)
     USERNAME=models.CharField(max_length=150)
     CATEGORY=models.CharField(max_length=50)

class  staff(models.Model):
       NAME=models.CharField(max_length=50)
       AGE=models.CharField(max_length=50)
       CONTACT=models.CharField(max_length=50)
       DATE_OF_BIRTH=models.CharField(max_length=50,null=True,blank=True)
       USERNAME=models.CharField(max_length=150)
       CATEGORY=models.CharField(max_length=50)

class   patients(models.Model):
       NAME=models.CharField(max_length=50)
       AGE=models.CharField(max_length=50)
       CONTACT=models.CharField(max_length=50)
       DATE_OF_BIRTH=models.CharField(max_length=50,null=True,blank=True)
       USERNAME=models.CharField(max_length=150)
       CATEGORY=models.CharField(max_length=50)

class BOOKING(models.Model):
      NAME=models.CharField(max_length=50)
      AGE=models.CharField(max_length=50)
      CONTACT=models.CharField(max_length=50)
      DATE_OF_BIRTH=models.CharField(max_length=50,null=True,blank=True)
      GENDER=models.CharField(max_length=50)
     


       
