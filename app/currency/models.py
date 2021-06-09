from django.db import models


class Rate(models.Model):
    type = models.CharField(max_length=5)
    source = models.CharField(max_length=64)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)


class ContactUS(models.Model):
    id = models.CharField(max_length=5)
    email_from = models.CharField(max_length=64)
    subject = models.DecimalField(max_digits=5, decimal_places=2)
    message = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)