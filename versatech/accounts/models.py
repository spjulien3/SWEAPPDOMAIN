from django.db import models
from django.contrib.auth.models import Group
from django.dispatch import receiver
from datetime import datetime as dt
import datetime
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

ROLE_GROUPS = ['is_manager', 'is_admin', 'is_accountant']

class AccountManager(BaseUserManager):
    def create_user(self, email, username,date_of_birth, first_name, last_name, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, first_name, last_name, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            username=username,
            date_of_birth=date_of_birth,
            
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    date_of_birth = models.DateField(verbose_name='date_of_birth')
    is_account_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    s_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ 'email','date_of_birth', 'first_name', 'last_name']

    objects = AccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

@receiver(pre_save, sender=Account)
def account_pre_save(sender, instance, **kwargs):
    created_date =dt.today().strftime('%m%d')
    instance.username = instance.first_name[0] + instance.last_name + created_date
    # instance.save()
    # tries = 3
    # for i in range(tries):
    #     try:
    #         if instance.is_admin:
    #             print()     
    #     except Group.Do
    
