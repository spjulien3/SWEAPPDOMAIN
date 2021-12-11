from django.shortcuts import render
from ledgerAccount.models import ledgerAccount, Journal

# Create your views here.
def chartofaccounts_view(request):
    context = {}
    model = ledgerAccount
    query = ledgerAccount.objects.all()
    context['accounts_query'] = query
    return render (request, 'chartofaccounts.html', context)

def journals_view(request):
    context = {}
    model = Journal
    query = Journal.objects.all()
    context['accounts_query'] = query
    return render (request, 'journals.html', context)