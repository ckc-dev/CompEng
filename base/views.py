"""Views for base app."""

import uuid
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.forms import SetPasswordForm
from django.core.mail import send_mail
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls import reverse

from . import forms, models, utils


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


def password_reset(request):
    if request.user.is_authenticated:
        logout(request)

    form = forms.PasswordResetRequestForm(request.POST or None)

    if request.method == 'POST':
        try:
            user = models.User.objects.get(email=request.POST.get('email'))
            current_datetime = datetime.utcnow()

            pw_reset_request = models.PasswordResetRequest.objects.create(
                user=user,
                timestamp=current_datetime,
                expiry=current_datetime + timedelta(hours=1),
                token=uuid.uuid4()
            )

            message = request.build_absolute_uri(reverse(
                'base:password_reset_confirm',
                kwargs={'token': pw_reset_request.token}
            ))

            send_mail(
                'Reset your unWaste password',
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user.email]
            )

            return redirect('base:password_reset_sent')
        except models.User.DoesNotExist:
            return redirect('base:password_reset_sent')

    context = {'page': 'reset', 'form': form}

    return render(request, 'base/password-reset.html', context)


def password_reset_sent(request):
    context = {'page': 'sent'}
    return render(request, 'base/password-reset.html', context)


def password_reset_confirm(request, token):
    pw_reset_request = models.PasswordResetRequest.objects.get(token=token)
    datetime_now = datetime.utcnow()

    if not pw_reset_request:
        return redirect('base:password_reset')

    if pw_reset_request.done:
        return redirect('base:password_reset')

    if pw_reset_request.expiry < datetime_now:
        return redirect('base:password_reset')

    user = pw_reset_request.user
    form = SetPasswordForm(user, request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            pw_reset_request.done = True
            pw_reset_request.save()

            return redirect('base:password_reset_done')

    context = {'page': 'confirm', 'form': form}

    return render(request, 'base/password-reset.html', context)


def password_reset_done(request):
    context = {'page': 'done'}
    return render(request, 'base/password-reset.html', context)


def user_logout(request):
    logout(request)
    return redirect('base:index')


def user_settings(request):
    return render(request, 'base/settings.html')


def about_us(request):
    return render(request, 'base/about-us.html')


def terms_of_service(request):
    return render(request, 'base/terms-of-service.html')


def privacy_policy(request):
    return render(request, 'base/privacy-policy.html')


def collection_request(request):
    user = request.user
    collection_requests = user.collection_requests.all()
    form = forms.CollectionRequestForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            r = form.save(commit=False)
            r.user = user
            r.save()

            return redirect('base:collection_request')

    context = {
        'collection_requests': collection_requests,
        'form': form,
    }

    return render(request, 'base/collection-request.html', context)
