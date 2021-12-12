from decimal import Context
import djmoney
from django.db.models import query
from django.shortcuts import redirect, render
from .forms import JournalEntryForm, JournalForm, ledgerAccountForm
from ledgerAccount.models import ledgerAccount, Journal, JournalEntry

# Create your views here.
def chartofaccounts_view(request):
    context = {}
    model = ledgerAccount
    query = ledgerAccount.objects.all()
    context['accounts_query'] = query
    return render (request, 'chartofaccounts.html', context)

def journals_view(request):
    context = {}
    journals = JournalEntry
 
    query =  journals.objects.all()
    context['accounts_query'] = query
    context [ 'zero'] = djmoney.money.Money(0,'USD')
    return render (request, 'journals.html', context)

def create_journal_entry_view(request, pk):
    context = {}
    journal_entry = JournalEntry
    journal = Journal.objects.get(id=pk)
    form = JournalEntryForm()
    if request.method == 'POST':
        
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('journals')
    context['journal_entry_form'] = form
    context['journal_entry'] = journal_entry
    context['journal']= journal
    return render(request, 'create_journal_entry.html', context)

def create_journal_view(request, pk):
    context = {}
    form = JournalForm()
    journal = Journal.objects.get(id=pk)
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('journals')
    context ['journal'] = journal    
    context ['journal_form'] = form
    return render(request, 'create_journal.html', context)

def create_ledger_account_view(request):
    context = {}
    form = ledgerAccountForm()
    model = ledgerAccount
    
    if request.method == 'POST':
        form = ledgerAccountForm(request.POST)
        
        if form.is_valid():
            model.createdby = request.user
            form.save()
            return redirect('chartofaccounts')
    context ['ledger_account'] = model
    context ['ledger_account_form'] = form
    return render(request, 'create_ledger_account.html', context)
