from django.db import models
# packages reqquired for Extended Model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Packages required to get default time
from django.utils import timezone
# Package required to create unique id for transactions
import uuid


class Account(models.Model):
    id = models.CharField(max_length=128, primary_key=True,
                          blank=True, unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128, default='Cash')
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    currency = models.CharField(max_length=4, default='BDT')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['user', 'name', 'type']

class BankAccount(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    bankName = models.CharField(max_length=128)
    bankBranch = models.CharField(max_length=128)
    bankAccountType = models.CharField(max_length=128)
    bankAccountName = models.CharField(max_length=128)
    bankAccountNumber = models.CharField(max_length=128)

class DigitalWallet(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    serviceName = models.CharField(max_length=128)
    serviceID = models.CharField(max_length=128)

class Transaction(models.Model):
    id = models.CharField(max_length=128, primary_key=True,
                          blank=True, unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now())
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type = models.CharField(max_length=8)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    reason = models.CharField(max_length=128)
    remark = models.CharField(max_length=256)

    def __str__(self):
        return self.id

# This Extended Model adds a few more attribtues to the predifined User Model of Django.
# This Model needs testing.


class Extended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_debit = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    total_credit = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)