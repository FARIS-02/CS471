from django.db import models

# 1. جدول شركة النشر (لازم يكون فوق)
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    
class Studio(models.Model):
    name = models.CharField(max_length=200)
    founded_date = models.DateField(null=True)

# جدول الألعاب (تم تحديثه ليتطابق مع طلبات Lab 9)
class Game(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    release_date = models.DateTimeField()
    rating = models.SmallIntegerField(default=1)
    
    # ربط اللعبة بشركة النشر (كل لعبة لها ناشر واحد)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    # ربط اللعبة باستديوهات التطوير (اللعبة ممكن يطورها أكثر من استديو)
    studios = models.ManyToManyField(Studio)

class Address(models.Model):
    city = models.CharField(max_length=50)


class Player(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)