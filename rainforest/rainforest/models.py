from django.db import models
from django import forms

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return "Name: {} Price: {} Description: {}".format(self.name, self.price, self.description)
