from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)