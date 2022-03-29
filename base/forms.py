from django import forms

from . import models


class RequirementForm(forms.ModelForm):
    class Meta:
        model = models.Requirement
        fields = (
            'author',
            'reference',
            'name',
            'category',
            'version',
            'priority',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(RequirementForm, self).__init__(*args, **kwargs)

        self.fields['author'].label = 'Seu nome'
        self.fields['reference'].label = 'Referência'
        self.fields['name'].label = 'Nome do requisito'
        self.fields['category'].label = 'Categoria do requisito'
        self.fields['version'].label = 'Versão do requisito'
        self.fields['priority'].label = 'Prioridade do requisito'
        self.fields['description'].label = 'Descrição do requisito'
