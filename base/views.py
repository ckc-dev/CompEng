"""Views for base app."""

from django.contrib.auth import login, logout
from django.db import IntegrityError
from django.shortcuts import redirect, render

from . import forms, utils


def index(request):
    return render(request, 'base/index.html')


def user_login(request):
    if request.user.is_authenticated:
        logout(request)

    form = forms.LoginForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            next = request.GET.get('next', 'base:index')
            user = form.get_user()

            login(request, user)
            return redirect(next)

    context = {'page': 'login', 'form': form}

    return render(request, 'base/authentication.html', context)


def user_register(request):
    if request.user.is_authenticated:
        logout(request)

    form = forms.RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            try:
                user = form.save(commit=False)
                if not user.is_business:
                    if utils.check_cpf(user.cpf):
                        user.save()
                        login(request, user)
                        return redirect('base:index')

                    form.add_error('cpf', 'Invalid CPF number.')
            except IntegrityError:
                form.add_error(None, 'This user is already registered.')

    context = {'page': 'register', 'form': form}

    return render(request, 'base/authentication.html', context)


def user_logout(request):
    logout(request)
    return redirect('base:index')


def settings(request):
    return render(request, 'base/settings.html')


def about_us(request):
    return render(request, 'base/about-us.html')


def terms_of_service(request):
    return render(request, 'base/terms-of-service.html')


def privacy_policy(request):
    return render(request, 'base/privacy-policy.html')
