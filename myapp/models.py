# myapp/models.py
from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    place_of_origin = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)