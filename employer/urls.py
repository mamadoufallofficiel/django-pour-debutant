
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_employers, name='liste_employers'),
    path('ajouter/', views.ajouter_employer, name='ajouter_employer'),
]
