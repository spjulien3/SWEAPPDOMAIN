from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegistrationForm
from accounts.forms import AccountAuthenticationForm
from accounts.forms import AccountUpdateForm
from decorators.decorators import allowed_users, unathenticated_user


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account_auth = authenticate(email=email,password=raw_password)
            login(request,account_auth)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request,'register.html', context)


def home(request):
    context = {}
    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password=password)

            if user:
                login(request,user)
                return redirect('home') 
    else:
        form = AccountAuthenticationForm
    context['login_form'] = form
    return render(request, 'login.html',context)

@allowed_users(allowed_roles=['Manager', 'Administrator', 'Accountant'])
def account_view(request):

    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
    else:
        form =  AccountUpdateForm(
            initial= {
                "email": request.user.email,
            }
        )
    context['account_form'] = form
    return render( request, 'account.html', context)

@allowed_users(allowed_roles=['Manager','Administrator'])
def chartofaccounts_view(request):
    context = {}
    return render(request,'chartofaccounts.html', context )