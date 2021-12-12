from django.urls import path
from . import views

urlpatterns = [
    path('chartofaccounts/', views.chartofaccounts_view, name='chartofaccounts'),
    path('journals/', views.journals_view, name='journals'),
    path('create_journal_entry/<str:pk>/', views.create_journal_entry_view, name='create_journal_entry'),
    path('create_journal/<str:pk>/', views.create_journal_view, name='create_journal'),
    path('create_ledger_account/', views.create_ledger_account_view, name='create_ledger_account'),
]