from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractUser, AbstractBaseUser, PermissionsMixin, UserManager)
#from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, UserManager
#from django.contrib.auth.models import *
# Create your models here.


class CustomUserManager(UserManager):
    def __create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You should have an email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        return self.__create_user(email, password, **extra_fields)
    
    def super_create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        return self.__create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    #username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.ImageField(default="avatar.png")
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ["-date_joined"]
    