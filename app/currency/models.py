from django.db import models


class Rate(models.Model):
    type = models.CharField(max_length=5)
    source = models.CharField(max_length=64)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)


class ContactUS(models.Model):
    # id no need to describe
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=64)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
