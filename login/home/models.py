from django.db import models

# Create your models here.
class User(models.Model):
    uK = models.AutoField(primary_key=True)
    uE = models.CharField(max_length=30)
    uP = models.CharField(max_length=40)

class LoggedUser(models.Model):
    u = models.ForeignKey(User, on_delete=models.CASCADE)
