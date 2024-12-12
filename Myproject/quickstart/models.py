from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address.")
        if not password:
            raise ValueError("Users must add a password.")
        
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_staffuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        user = self.create_user(
            email,
            password=password,
            **extra_fields
        )
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin = True')
        
        user = self.create_user(
            email,
            password=password,
            **extra_fields
        )

        return user



class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
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
