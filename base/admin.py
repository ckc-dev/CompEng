"""Register 'base' app models to Django's admin panel."""

from django.contrib import admin

from . import models

admin.site.register(models.Reference)
admin.site.register(models.Requirement)
