from django.urls import path
from . import views

urlpatterns = [
    path('chartofaccounts/', views.chartofaccounts_view, name='chartofaccounts'),
    path('journals/', views.journals_view, name='journals'),
]