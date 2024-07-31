from django.db import models

class students(models.Model):
    name = models.CharField(max_length=100)
    reg = models.CharField(max_length=100)
    sem1 = models.IntegerField(default=0)
    sem2 = models.IntegerField(default=0)
    sem3 = models.IntegerField(default=0)
    sem4 = models.IntegerField(default=0)
    sem5 = models.IntegerField(default=0)
    sem6 = models.IntegerField(default=0)
    sem7 = models.IntegerField(default=0)
    sem8 = models.IntegerField(default=0)
