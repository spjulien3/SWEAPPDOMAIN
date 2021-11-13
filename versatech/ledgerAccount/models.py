# from django.db import models
from django.db import models
import uuid

# Create your models here.
class ledgerAccount(models.Model):
    account_name = models.CharField(max_length=50)
    account_number = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid.uuid4)
    account_description = models.CharField(max_length=100)
    normal_side = models.FloatField()
    account_category =  models.CharField(max_length=100)
    account_subcategory = models.CharField(max_length=100)
    debit = models.FloatField()
    credit = models.FloatField()
    balance = models.FloatField()
    date_account_added = models.DateTimeField(auto_now_add=True)
    order = models.FloatField()
    statement = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)