"""Views for 'base' app."""

from django.contrib import messages
from django.shortcuts import render

from . import forms, models


def index(request):
    """
    View for index page.

    Args:
        request (HttpRequest): Request made by user.

    Returns:
        HttpResponse: Rendered page.
    """
    references = models.Reference.objects.all().order_by('pk')
    requirements = models.Requirement.objects.all().order_by('-date')
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


def latex(request):
    """
    View for page containing LaTeX representation of requirements.

    Args:
        request (HttpRequest): Request made by user.

    Returns:
        HttpResponse: Rendered page.
    """
    requirements = models.Requirement.objects.all().order_by('section')
    sections = set(requirements.values_list('section', flat=True))
    string = ''

    for section in sections:
        functional_requirement_id = 1
        non_functional_requirement_id = 1
        string += f'\\section{{{section}}}'

        for requirement in requirements:
            if requirement.section != section:
                continue
            if requirement.type == 'RF':
                string += requirement.to_latex(functional_requirement_id)
                functional_requirement_id += 1
            else:
                string += requirement.to_latex(non_functional_requirement_id)
                non_functional_requirement_id += 1
        string += '\n'

    context = {'string': string}

    return render(request, 'base/latex.html', context)
