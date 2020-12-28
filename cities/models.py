from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=250)

    class Meta():
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    class Meta():
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name
