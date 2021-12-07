from django.conf import settings
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.enums import Choices
from djmoney.models.fields import MoneyField
import uuid

NORMAL_SIDE_CHOICES = (
    ("1","RIGHT"),("2","LEFT"),
)

ACCOUNT_CATEGORY_CHOICES = (
    ("1","ASSETS"), ("2","LIABILITIES"),
    ("3","EQUITY"), ("4","INCOME"),
    ("5","EXPENSE"), ("6","REVENUE"),
)

ACCOUNT_SUBCATEGORY_CHOICES = (
    ("1","CURRRENT ASSETS"), ("2","FIXED ASSETS"), 
    ("3","LONG TERM ASSETS"), ("4","ACCOUNTS RECIEVABLE"),
    ("5","CURRENT LIABILITIES"), ("6","PAYROLL LIABILITIES"),
    ("7","LONG TERM LIABILITIES"), ("8","NOTES PAYABLE"),
    ("9","ACCRUED EXPENSES"), ("10","DEFFERED REVENUE"),
    ("11","COMMON STOCK"), ("12","PREFERRED STOCK"),
    ("13","RETAINED EARNINGS"), ("14","DIVIDENDS"),
    ("15","TREASURY STOCK"),
)



# Create your models here.
class ledgerAccount(models.Model):
    account_number = models.IntegerField(default=0)
    account_name = models.CharField(max_length=50)
    account_description = models.CharField(max_length=100)
    normal_side = models.CharField(max_length=5, choices=NORMAL_SIDE_CHOICES)
    account_category =  models.CharField(max_length=100, choices=ACCOUNT_CATEGORY_CHOICES)
    account_subcategory = models.CharField(max_length=100, choices=ACCOUNT_SUBCATEGORY_CHOICES)
    debit = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True)
    credit = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True)
    date_account_added = models.DateTimeField(auto_now_add=True)
    statement = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
    is_approved =  models.BooleanField(default=False)

    def __str__(self):
        return self.account_name