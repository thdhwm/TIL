from django.db import models

# Create your models here.

class Gacha(models.Model):

    name = models.CharField(max_length=50)

    game = models.CharField(max_length=50)

    description = models.TextField()

    urgency = models.FloatField()
