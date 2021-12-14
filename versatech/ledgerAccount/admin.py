from django.contrib import admin
from ledgerAccount.models import ledgerAccount, JournalEntry

admin.site.register(ledgerAccount)
# admin.site.register(Journal)
admin.site.register(JournalEntry)
