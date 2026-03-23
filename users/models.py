from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True) # 'admin', 'client', 'manager'
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    middle_name = models.CharField(max_length=150, blank=True)
    
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
   
    roles = models.ManyToManyField(Role, related_name="users", blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email