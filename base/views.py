"""Views for base app."""

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from . import forms


def index(request):
    return render(request, 'base/index.html')


def user_login(request):
    if request.user.is_authenticated:
        logout(request)

    form = AuthenticationForm(request, data=request.POST or None)

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
            user = form.save()

            login(request, user)
            return redirect('base:index')

    context = {'form': form}

    return render(request, 'base/authentication.html', context)


def user_logout(request):
    logout(request)
    return redirect('base:index')
