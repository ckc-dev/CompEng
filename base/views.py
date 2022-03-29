from django.contrib import messages
from django.shortcuts import HttpResponse, render

from . import forms, models


def index(request):
    references = models.Reference.objects.all().order_by('pk')
    requirements = models.Requirement.objects.all()
    form = forms.RequirementForm(request.POST or None)
    context = {
        'form': form,
        'references': references,
        'requirements': requirements,
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Requisito levantado.'
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Formulário inválido, tente novamente.'
            )

    return render(request, 'base/index.html', context)
