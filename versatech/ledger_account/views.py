from django.shortcuts import render
from ledger_account.models import ledgerAccount

# Create your views here.
def dashboard_view(request):
    context = {}
    model = ledgerAccount
    query = ledgerAccount.objects.all()
    context['accounts_query'] = query
    return render (request, 'dashboard.html', context)

