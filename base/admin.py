from django.contrib import admin

from . import models

admin.site.register(models.Available)
admin.site.register(models.Requirement)
