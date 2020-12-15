from django.db import models

# Create your models here.

class Fighter(models.Model):
    name = models.CharField(max_length=100)
    hp = models.CharField(max_length=100)
    weapon = models.CharField(max_length=100)
    armor = models.CharField(max_length=100)
    money = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Wizard(models.Model):
    name = models.CharField(max_length=100)
    hp = models.CharField(max_length=100)
    weapon = models.CharField(max_length=100)
    armor = models.CharField(max_length=100)
    money = models.CharField(max_length=100)
    magic = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name