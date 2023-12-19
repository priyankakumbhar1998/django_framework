from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20)
    contact = models.IntegerField()
    address = models.TextField()
    
