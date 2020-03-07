from django.db import models
from django import VERSION
# admin admin@mail.ru admin

class Product(models.Model):
    name = models.CharField(max_length=255)
    #email = models.EmailField()
    price = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        print(VERSION,"versio")
        return "{} {} {}".format(self.name, self.volume, self.price)
