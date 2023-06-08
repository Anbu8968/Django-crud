from django.db import models
from django.contrib.auth.hashers import make_password,check_password


class User(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    email=models.CharField(max_length=200,null=False,blank=False)
    password=models.CharField(max_length=500,null=False,blank=False)


    def __str__(self):
        return self.name