from django.db import models
from django.contrib import admin
# Create your models here.
class User(models.Model):
    users = models.CharField(max_length=100)


class Passwords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

admin.site.register(User)
admin.site.register(Passwords)