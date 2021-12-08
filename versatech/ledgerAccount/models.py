from django.conf import settings
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.enums import Choices
from djmoney.models.fields import MoneyField
import uuid

NORMAL_SIDE_CHOICES = (
    ("RIGHT","RIGHT"),("LEFT","LEFT"),
)

ACCOUNT_CATEGORY_CHOICES = (
    ("ASSETS","ASSETS"), ("LIABILITIES","LIABILITIES"),
    ("EQUITY","EQUITY"), ("INCOME","INCOME"),
    ("EXPENSE","EXPENSE"), ("REVENUE","REVENUE"),
)

ACCOUNT_SUBCATEGORY_CHOICES = (
    ("CURRRENT ASSETS","CURRRENT ASSETS"), ("FIXED ASSETS","FIXED ASSETS"), 
    ("LONG TERM ASSETS","LONG TERM ASSETS"), ("ACCOUNTS RECIEVABLE","ACCOUNTS RECIEVABLE"),
    ("CURRENT LIABILITIES","CURRENT LIABILITIES"), ("PAYROLL LIABILITIES","PAYROLL LIABILITIES"),
    ("LONG TERM LIABILITIES","LONG TERM LIABILITIES"), ("NOTES PAYABLE","NOTES PAYABLE"),
    ("ACCRUED EXPENSES","ACCRUED EXPENSES"), ("DEFFERED REVENUE","DEFFERED REVENUE"),
    ("COMMON STOCK","COMMON STOCK"), ("PREFERRED STOCK","PREFERRED STOCK"),
    ("RETAINED EARNINGS","RETAINED EARNINGS"), ("DIVIDENDS","DIVIDENDS"),
    ("TREASURY STOCK","TREASURY STOCK"),
)



# Create your models here.
class ledgerAccount(models.Model):
    account_number = models.CharField(max_length=3,default=0)
    account_name = models.CharField(max_length=50)
    account_description = models.CharField(max_length=100, blank=True )
    normal_side = models.CharField(max_length=5, choices=NORMAL_SIDE_CHOICES)
    account_category =  models.CharField(max_length=100, choices=ACCOUNT_CATEGORY_CHOICES)
    account_subcategory = models.CharField(max_length=100, choices=ACCOUNT_SUBCATEGORY_CHOICES, blank=True)
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