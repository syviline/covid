from django.db import models

# Create your models here.

class CountryStatistics(models.Model):
    country = models.CharField(max_length=255)
    cases = models.IntegerField()
    todayCases = models.IntegerField()
    deaths = models.IntegerField()
    todayDeaths = models.IntegerField()
    recovered = models.IntegerField()
    todayRecovered = models.IntegerField()
    active = models.IntegerField()
    updated = models.IntegerField()
    updatedClient = models.IntegerField(default=0)
    json = models.TextField()


class ipCountries(models.Model):
    ip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class HistoricData(models.Model):
    country = models.CharField(max_length=255)
    data = models.TextField()
    updatedClient = models.IntegerField(default=0)


class TopCountries(models.Model):
    data = models.TextField()


class Regions(models.Model):
    data = models.TextField()
    lastUpdated = models.IntegerField()