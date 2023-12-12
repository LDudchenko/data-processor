from django.db import models

# Create your models here.

class StatsModel(models.Model):
    param = models.CharField(max_length=255)