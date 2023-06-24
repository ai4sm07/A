from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for User Profile"""
    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User Email required')
        else:
            email = self.normalize_email(email)
            user = self.model(email=email,name=name)

            user.set_password(password)
            user.save(using=self._db)

            return user
        
 
    def create_superuser(self,email,name,password):
        """Create Super User"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database form User of the App"""
    email =models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=16)
    is_activate = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive full name of the user"""
        return self.name
    
    def get_shot_name(self):
        """Retrive short of the user"""
        return self.name
    
    def __str__(self):
        """Return string representation of user"""
        return self.email