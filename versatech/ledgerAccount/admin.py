from django.contrib import admin
from ledgerAccount.models import ledgerAccount, Journal, JournalEntry

admin.site.register(ledgerAccount)
admin.site.register(Journal)
admin.site.register(JournalEntry)
