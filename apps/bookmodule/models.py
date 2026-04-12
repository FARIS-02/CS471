from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    developer = models.CharField(max_length=50) 
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)