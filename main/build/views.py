from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    context = {
        "title": "Home"
    }
    return render(request, 'home.html', context)

def mich(request):
    context = {
        "title": "Über mich"
    }
    return render(request, 'mich.html', context)

def kontakt(request):
    context = {
        "title": "Kontakt"
    }
    return render(request, 'kontakt.html', context)

def arbeit(request):
    context = {
        "title": "Meine Arbeit"
    }
    return render(request, 'arbeit.html', context)


