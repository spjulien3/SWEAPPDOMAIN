from django import forms
from django.forms.widgets import DateInput
from .models import JournalEntry, Journal, ledgerAccount
from django.forms import inlineformset_factory


class JournalEntryForm(forms.ModelForm):
    
    class Meta:
        model = JournalEntry
        fields = ("account_name", "journal","date", "debit", "credit")

class JournalForm(forms.ModelForm):
    
    class Meta:
        model = Journal
        fields = ("journal_name", "journal_balance" )

class ledgerAccountForm(forms.ModelForm):

    date_account_added = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model = ledgerAccount
        fields = (
            "account_number", "account_name",
            "account_description", "account_category",
            "date_account_added", "statement",
            "comment", "createdby", 
        
        )
    
    
