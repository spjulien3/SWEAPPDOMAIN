from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
	def create_user(self, email, date_joined, last_login, username,date_of_birth, first_name, last_name, password):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
            username=first_name+last_name+date_joined.date,
            password=password

		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, date_joined, last_login, date_of_birth, first_name, last_name, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
            first_name=first_name,
            last_name=last_name,
			username=first_name+last_name+date_joined.date,
            date_of_birth=date_of_birth,
            
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=False)
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
    s_superuser= models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'date_of_birth', 'first_name', 'last_name']

    objects = AccountManager()

    def __str__(self):
	    return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
	    return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
	    return True
