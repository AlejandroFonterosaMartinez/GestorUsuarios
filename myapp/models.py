from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_joined = models.DateTimeField()
    is_staff = models.BooleanField()
