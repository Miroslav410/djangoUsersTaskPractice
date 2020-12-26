from django.db import models, signals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.utils.crypto import get_random_string

from django.contrib.auth.models import User


from django.conf import settings

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,

            employee_id=get_random_string(length=32)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,

        )

        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email                       = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username                    = models.CharField(max_length=30, unique=True)
    date_joined                 = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login                  = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin                    = models.BooleanField(default=False)
    is_active                   = models.BooleanField(default=True)
    is_staff                    = models.BooleanField(default=False)
    is_superuser                = models.BooleanField(default=False)
    # first_name                  = models.CharField(max_length=30)
    employee_id                 = models.CharField(max_length=32, unique=True, default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    # def user_login_counter(self):

    def login_user(request, user):
        """
        Log in a user without requiring credentials (using ``login`` from
        ``django.contrib.auth``, first finding a matching backend).

        """
        from django.contrib.auth import load_backend, login
        if not hasattr(user, 'backend'):
            for backend in settings.AUTHENTICATION_BACKENDS:
                if user == load_backend(backend).get_user(user.pk):
                    user.backend = backend
                    break
        if hasattr(user, 'backend'):
            return login(request, user)
