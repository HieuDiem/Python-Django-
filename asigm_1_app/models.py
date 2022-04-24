
from dataclasses import field
from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=11)

    def __str__(self):
        return self.name
    

class Person3(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Manufacture(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    color = models.CharField(max_length=20)
    date_created = models.DateTimeField()
    
    def __str__(self):
        return self.name

class Car(models.Model):
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    date_created = models.DateTimeField()
    def __str__(self):
        return self.name