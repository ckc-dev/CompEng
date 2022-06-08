"""URL configuration for base app."""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-reset/sent/',
         views.password_reset_sent,
         name='password_reset_sent'),
    path('password-reset/confirm/<uuid:token>/',
         views.password_reset_confirm,
         name='password_reset_confirm'),
    path('password-reset/done/',
         views.password_reset_done,
         name='password_reset_done'),
    path('settings/', views.user_settings, name='settings'),
    path('about-us/', views.about_us, name='about_us'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('collection-request/',
         views.collection_request,
         name='collection_request'),
]
