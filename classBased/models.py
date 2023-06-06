from django.db import models

class user(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    email=models.CharField(max_length=200,null=False,blank=False)
    company=models.CharField(max_length=200,null=False,blank=False)


    def __str__(self):
        return self.name