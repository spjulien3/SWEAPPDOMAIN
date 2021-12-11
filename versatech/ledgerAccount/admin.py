from django.contrib import admin
from ledgerAccount.models import ledgerAccount, Journal

admin.site.register(ledgerAccount)
admin.site.register(Journal)
