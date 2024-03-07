from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Meine-Arbeit/', views.arbeit, name="arbeit"),
    path('Über-mich/', views.mich, name="mich"),
    path('Kontakt/', views.kontakt, name="kontakt"),
]
