from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    context = {
        "title": "Home"
    }
    return render(request, 'home.html', context)

def uns(request):
    context = {
        "title": "Über Uns"
    }
    return render(request, 'uns.html', context)

def kontakt(request):
    context = {
        "title": "Kontakt"
    }
    return render(request, 'kontakt.html', context)

def mitglied(request):
    context = {
        "title": "Mitglied werden"
    }
    return render(request, 'mitglied.html', context)


