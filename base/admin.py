from django.contrib import admin

from . import models


class userAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf_clean')


admin.site.register(models.User, userAdmin)
