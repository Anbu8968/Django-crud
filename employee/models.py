from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    