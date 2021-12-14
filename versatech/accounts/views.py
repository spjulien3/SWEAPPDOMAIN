from django.contrib import auth
from django.db.models import query
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegistrationForm
from accounts.forms import AccountAuthenticationForm
from accounts.forms import AccountUpdateForm
from decorators.decorators import allowed_users, unathenticated_user
from .models import Account
from django.core.mail import send_mail


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            # account_auth = authenticate(username=username,password=raw_password)
            login(request,user)
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
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)

            if user:
                login(request,user)
                return redirect('home') 
    else:
        form = AccountAuthenticationForm
    context['login_form'] = form
    return render(request, 'login.html',context)

@allowed_users(allowed_roles=['is_manager', 'is_admin', 'is_accountant'])
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

# @allowed_users['is_manager', 'is_admin', 'is_accountant']
def account_list_view (request):
    context = {}
    query = Account.objects.all()

    context ['accounts'] = query
    return render(request, "account_list.html", context)

def index(request):
    send_mail('Hello from VersaTech', 
    'Hello there. This is from VersaTech.', 
    'myversatech@gmail.com', 
    ['marcusimomio@gmail.com'], 
    fail_silently=False)

    return render(request, 'registration/password_reset_done.html')