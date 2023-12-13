from django.db import models

# Create your models here.

class DustFields(models.Model):
    PM1 = models.FloatField()
    PM2 = models.FloatField()
    PM10 = models.FloatField()


class DustModel(models.Model):
     _id=models.AutoField(primary_key=True)
     timestamp=models.DateTimeField()
     PM1 = models.FloatField()
     PM2 = models.FloatField()
     PM10 = models.FloatField()


class StatsModel(models.Model):
    timestamp=models.DateTimeField()
    temperature=models.FloatField()
    humidity=models.FloatField()
    CO2=models.FloatField()

class TemperatureModel(models.Model):
    _id=models.AutoField(primary_key=True)
    timestamp=models.DateTimeField()
    temperature=models.FloatField()

class HumidityModel(models.Model):
    _id=models.AutoField(primary_key=True)
    timestamp=models.DateTimeField()
    humidity=models.FloatField()

class CO2Model(models.Model):
    _id=models.AutoField(primary_key=True)
    timestamp=models.DateTimeField()
    CO2=models.FloatField()

    


