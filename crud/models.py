from django.db import models

# Create your models here.

class Member(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    userid=models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

