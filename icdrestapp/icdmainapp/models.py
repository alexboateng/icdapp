from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class  ICDVersion(models.Model):
    version = models.IntegerField(default=1, unique=True, validators=[MinValueValidator(1), MaxValueValidator(100000)])


class  ICDCode(models.Model):
    categoryCode = models.TextField(blank=False, default='')
    diagnosisCode = models.TextField(blank=False, default='')
    fullCode = models.TextField(blank=False, default='')
    abbrDesc = models.TextField(blank=False, default='')
    fullDesc = models.TextField(blank=False, default='')
    categoryTitle = models.TextField(blank=False, default='')
    appVersion = models.IntegerField(blank=False, default=9)

    # class Meta:
    #     unique_together = ('appVersion', 'diagnosisCode')