from django import forms
from ledger_account.models import ledgerAccount

# class NewLedgerAccountForm(forms.ModelForm):
#     account_name = forms.CharField(max_length=50)
#     account_description =  forms.CharField(max_length=100)
#     normal_side =  forms.FloatField()
#     account_category =   forms.CharField(max_length=100)
#     account_subcategory =  forms.CharField(max_length=100)
#     debit =  forms.FloatField()
#     credit =  forms.FloatField()
#     balance =  forms.FloatField()
#     order =  forms.FloatField()
#     statement =  forms.CharField(max_length=100)
#     comment =  forms.CharField(max_length=200)
#     class Meta:
#         model = ledgerAccount
#         fields = (
#             'account_name', 'account_description','normal_side','account_category',
#             'account_subcategory','debit','credit','balance','order','statement','comment'
#     )
