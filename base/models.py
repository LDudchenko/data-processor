from django.db import models

# Create your models here.

class DustModel(models.Model):
     timestamp=models.DateTimeField()
     PM1=models.FloatField()
     PM2=models.FloatField()
     PM10=models.FloatField()

class StatsModel(models.Model):
    timestamp=models.DateTimeField()
    temperature=models.FloatField()
    humidity=models.FloatField()
    CO2=models.FloatField()

class TemperatureModel(models.Model):
    timestamp=models.DateTimeField()
    temperature=models.FloatField()

class HumidityModel(models.Model):
    timestamp=models.DateTimeField()
    humidity=models.FloatField()

class CO2Model(models.Model):
    timestamp=models.DateTimeField()
    CO2=models.FloatField()

    


