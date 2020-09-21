from django.db import models


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    STR = models.IntegerField()
    AGL = models.IntegerField()
    WILL = models.IntegerField()
    LOG = models.IntegerField()
    CHA = models.IntegerField()
    EDG = models.IntegerField()
    ShadowAmp = models.ManyToManyField('ShadowAmp')

    class Meta:
        verbose_name_plural = 'characters'


class ShadowAmp(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = 'shadowamps'
