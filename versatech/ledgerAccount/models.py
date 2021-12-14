from operator import mod
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.db.models.fields.related import ForeignKey
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.enums import Choices
from djmoney.models.fields import MoneyField
from datetime import datetime as dt
from django.contrib.auth import get_user_model
import djmoney.money

import uuid

NORMAL_SIDE_CHOICES = (
    ("RIGHT","RIGHT"),("LEFT","LEFT"),("BALANCED","BALANCED")
)

ACCOUNT_CATEGORY_CHOICES = (
    ("ASSETS","ASSETS"), ("LIABILITIES","LIABILITIES"),
    ("EQUITY","EQUITY"), ("INCOME","INCOME"),
    ("EXPENSE","EXPENSE"), ("REVENUE","REVENUE"),
)

ACCOUNT_SUBCATEGORY_CHOICES = (
    ("CURRRENT","CURRRENT"), ("FIXED","FIXED"), 
    ("LONG TERM","LONG TERM"), ("ACCOUNTS RECIEVABLE","ACCOUNTS RECIEVABLE"),
    ("NOTES PAYABLE","NOTES PAYABLE"),
    ("ACCRUED","ACCRUED"), ("DEFFERED REVENUE","DEFFERED REVENUE"),
    ("COMMON STOCK","COMMON STOCK"), ("PREFERRED STOCK","PREFERRED STOCK"),
    ("RETAINED EARNINGS","RETAINED EARNINGS"), ("DIVIDENDS","DIVIDENDS"),
    ("TREASURY STOCK","TREASURY STOCK"),
)


# Create your models here.
class ledgerAccount(models.Model):
    account_number = models.IntegerField(max_length=3,default=0, primary_key=True)
    account_name = models.CharField(max_length=50)
    account_description = models.CharField(max_length=100, blank=True )
    normal_side = models.CharField(max_length=10, choices=NORMAL_SIDE_CHOICES, blank=True)
    account_category =  models.CharField(max_length=100, choices=ACCOUNT_CATEGORY_CHOICES)
    account_subcategory = models.CharField(max_length=100, choices=ACCOUNT_SUBCATEGORY_CHOICES, blank=True)
    debit = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True,default=djmoney.money.Money(0,'USD'))
    credit = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True,default=djmoney.money.Money(0,'USD'))
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True,default=djmoney.money.Money(0,'USD'))
    date_account_added = models.DateField(default=dt.now)
    statement = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    createdby = models.ForeignKey(get_user_model(), on_delete=PROTECT)
    is_approved =  models.BooleanField(default=False)

    def __str__(self):
        return self.account_name

class JournalEntry(models.Model):

    date = models.DateField(default=dt.now)
    account_name = models.ForeignKey(ledgerAccount, on_delete=PROTECT)
    date = models.DateField(default=dt.now)
    post_reference = models.AutoField(primary_key=True)
    normal_side = models.CharField(max_length=10, choices=NORMAL_SIDE_CHOICES)
    debit = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True,default=djmoney.money.Money(0,'USD'))
    credit = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True,default=djmoney.money.Money(0,'USD'))
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True, default=djmoney.money.Money(0,'USD'))
    is_approved = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=True)
    reason = models.CharField(max_length=100, blank=True)


@receiver(pre_save, sender=JournalEntry)
def journal_entry_presave( sender, instance, **kwargs):
    query = JournalEntry.objects.all()
    balance = djmoney.money.Money(0,'USD')
    max = djmoney.money.Money(0,'USD')
    print(balance)
    for index in query:
        if max < index.balance and index.account_name == instance.account_name:
            max = index.balance
            balance = index.balance
    if (instance.debit > djmoney.money.Money(0,'USD')):
        instance.balance = balance + instance.debit
    if (instance.credit > djmoney.money.Money(0,'USD')):
        instance.balance = balance - instance.credit
    
    if(instance.debit > instance.credit):
        instance.normal_side = "LEFT"
    if(instance.credit < instance.debit):
        instance.normal_side = "RIGHT"
    instance.account_name.save()


@receiver(pre_save, sender=ledgerAccount)
def balance_update( sender, instance, **kwargs):
    query = JournalEntry.objects.all()
    balance_sum = djmoney.money.Money(0,'USD')
    max = djmoney.money.Money(0,'USD')
    print(balance_sum)
    
    for index in query:
        if max < index.balance:
            max = index.balance
            balance_sum = index.balance
    instance.balance = balance_sum
    if (instance.debit > djmoney.money.Money(0,'USD')):
        instance.balance = balance_sum + instance.debit
    if (instance.credit > djmoney.money.Money(0,'USD')):
        instance.balance = balance_sum - instance.credit

    if(instance.balance > djmoney.money.Money(0,'USD')):
        instance.normal_side = "LEFT"
    if(instance.balance > djmoney.money.Money(0,'USD')):
        instance.normal_side = "RIGHT"
    if(instance.balance == djmoney.money.Money(0,'USD')):
        instance.normal_side = "BALANCED"

# @receiver(post_save, sender=JournalEntry)
# def journal_entry_balance_update(sender, instance, **kwargs):
#     account = instance.ledgerAccount_set.all()
#     query = instance.objects.all()
#     balance_sum = djmoney.money.Money(0,'USD')
#     max = djmoney.money.Money(0,'USD')
#     print(balance_sum)
#     for index in query:
#         if max < index.balance:
#             max = index.balance
#             balance_sum = index.balance
    

#     if (instance.debit > djmoney.money.Money(0,'USD')):
#         instance.balance = balance_sum + instance.debit
#     if (instance.credit > djmoney.money.Money(0,'USD')):
#         instance.balance = balance_sum - instance.credit

#     instance.balance = balance_sum
#     account.balance = balance_sum
#     account.save()
#     print(account.balance)
