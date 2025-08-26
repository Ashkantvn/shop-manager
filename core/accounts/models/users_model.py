from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=False, null=False,db_index=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)        

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    REQUIRED_FIELDS = ['first_name', 'last_name']