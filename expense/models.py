from django.db import models

# Create your models here.
class Expense(models.Model):
    expense = models.CharField(max_length=60)
    price = models.FloatField()
