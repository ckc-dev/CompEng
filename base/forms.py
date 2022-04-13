from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'name',
            'email',
            'is_business',
            'cpf',
            'cnpj',
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['cpf'].label = 'CPF'
        self.fields['cnpj'].label = 'CNPJ'

    def clean(self):
        data = self.cleaned_data
        is_business = data.get('is_business')
        cpf = data.get('cpf')
        cnpj = data.get('cnpj')

        if is_business and not cnpj:
            self.add_error('cnpj', 'Please insert your CNPJ.')
        elif not is_business and not cpf:
            self.add_error('cpf', 'Please insert your CPF.')
        else:
            return data
