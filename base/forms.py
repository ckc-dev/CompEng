from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    cpf = forms.CharField(required=True, min_length=11, max_length=14)

    class Meta:
        model = get_user_model()
        fields = ("name", "email", "cpf", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['cpf'].label = 'CPF'

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs, commit=False)
        user.email = self.cleaned_data["email"]
        user.save()

        return user
