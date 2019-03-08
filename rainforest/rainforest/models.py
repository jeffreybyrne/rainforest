from django.db import models
from django import forms

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return "Name: {} Price: {} Description: {}".format(self.name, self.price, self.description)


    def price_in_dollars(self):
        dollars = self.price / 100
        return "${:.2f}".format(dollars)


class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return "Comment: {} At: {} ".format(self.comment, self.created_at)
