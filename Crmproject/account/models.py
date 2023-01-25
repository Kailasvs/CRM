from django.db import models

# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=1024)

class State(models.Model):
    name=models.CharField(max_length=1024)

class Nationality(models.Model):
    name=models.CharField(max_length=1024)
    
    
    