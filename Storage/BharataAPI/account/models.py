from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True, max_length=250)
    
    REQUIRED_FIELDS=('email','first_name','last_name',)

    def __str__(self) -> str:
        return self.username