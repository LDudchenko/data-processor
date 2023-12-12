from django.db import models

class DataModel(models.Model):
    param = models.CharField(max_length=255)