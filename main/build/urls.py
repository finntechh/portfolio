from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Mitglied-werden/', views.mitglied, name="mitglied"),
    path('Über-uns/', views.uns, name="uns"),
    path('Kontakt/', views.kontakt, name="kontakt"),
]
