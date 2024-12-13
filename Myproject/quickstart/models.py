from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    username = models.CharField(blank=True, unique=True, max_length=50)
    email = models.EmailField(unique=True, blank=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [email]

    objects = UserManager()

    def __str__(self):
        return self.email
    

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True


class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=512)
    refresh_token = models.CharField(max_length=512)

    def __str__(self):
        return f"Tokens for {self.user.username}"