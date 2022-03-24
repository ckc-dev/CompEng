import re

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    is_business = models.BooleanField(default=False)
    cpf = models.CharField(null=True, blank=True, unique=True, max_length=14)
    cnpj = models.CharField(null=True, blank=True, unique=True, max_length=18)
    cpf_clean = models.BigIntegerField(null=True, blank=True, unique=True)
    cnpj_clean = models.BigIntegerField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        # Temporary fix, make sure to address this later.
        self.username = self.email

        if self.cpf:
            self.cpf_clean = int(re.sub(r'\D', '', self.cpf))
        if self.cnpj:
            self.cnpj_clean = int(re.sub(r'\D', '', self.cnpj))
        super(User, self).save(*args, **kwargs)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
