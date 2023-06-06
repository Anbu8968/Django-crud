from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    age=models.IntegerField()
    weight=models.IntegerField()
    height=models.IntegerField()

    def __str__(self):
        return self.name