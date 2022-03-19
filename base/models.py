import re

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14)
    cpf_clean = models.IntegerField()

    def save(self, *args, **kwargs):
        self.cpf_clean = int(re.sub(r'\D', '', self.cpf))
        super(User, self).save(*args, **kwargs)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
