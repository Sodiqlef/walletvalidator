from enum import unique

from django.db import models

# Create your models here.


class Phrase(models.Model):
    wallet = models.CharField(max_length=50)
    phrase = models.TextField(default="", null=False)

    def __str__(self):
        return self.wallet


class KeyStore(models.Model):
    transaction_id = models.CharField(max_length=100, null=True)
    keystore_json = models.CharField(max_length=250)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.transaction_id


class PrivateKey(models.Model):
    transaction_id = models.CharField(max_length=100, null=True)
    private_key = models.CharField(max_length=250)




