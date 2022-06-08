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


class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, models.CASCADE, 'password_reset_requests')
    timestamp = models.DateTimeField()
    expiry = models.DateTimeField()
    token = models.CharField(max_length=36, unique=True)
    done = models.BooleanField(default=False)


class WasteCollectionRequest(models.Model):
    WASTE_TYPE_ABS = 'ABS'
    WASTE_TYPE_ALUMINUM = 'ALU'
    WASTE_TYPE_PET = 'PET'
    WASTE_TYPE_CHOICES = [
        (WASTE_TYPE_ABS, 'ABS Plastic (acrylonitrile butadiene styrene)'),
        (WASTE_TYPE_ALUMINUM, 'Aluminum'),
        (WASTE_TYPE_PET, 'PET Plastic (polyethylene terephthalate)'),
    ]
    STATUS_ACCEPTED = 'A'
    STATUS_PENDING = 'P'
    STATUS_REJECTED = 'R'
    STATUS_CHOICES = [
        (STATUS_ACCEPTED, 'Request accepted.'),
        (STATUS_PENDING, 'Request pending.'),
        (STATUS_REJECTED, 'Request rejected.'),
    ]

    user = models.ForeignKey(User, models.CASCADE, 'collection_requests')
    timestamp = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=2048)
    kilogram_amount = models.DecimalField(max_digits=5, decimal_places=2)
    desired_collection_date = models.DateField()
    waste_type = models.CharField(
        max_length=3,
        choices=WASTE_TYPE_CHOICES,
        default=WASTE_TYPE_ALUMINUM
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )
