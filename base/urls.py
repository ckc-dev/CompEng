"""URL patterns for 'base' app."""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('latex', views.latex, name='latex'),
]
