from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration_view, name='registration'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('account/', views.account_view, name='account'),
    path('account_list/', views.account_list_view, name='account_list'),
    path('', views.home),
    path('', views.index),
]