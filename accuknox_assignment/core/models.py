from django.db import models

# Question 1 and 2 Code
class TestModel(models.Model):
    name = models.CharField(max_length=100)

# Question 3 Code
class SignalLog(models.Model):

    message = models.CharField(max_length=100)