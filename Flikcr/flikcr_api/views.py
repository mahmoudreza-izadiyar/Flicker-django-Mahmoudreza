from django.shortcuts import render
from .models import Preset, FavouritePlaces

# Create your views here.

def index(request):
    presets = Preset.objects.all()
    context = {
        "presets": presets,
    }
    return render(request, 'flikcr_api/index.html', context)


def favourites(request):
    favourites = FavouritePlaces.objects.all()
    context = {
        "favourites": favourites,
    }
    return render(request, 'flikcr_api/fav.html', context)



def edit(request):
    context = {
        "name": "mahmoudreza",
    }
    return render(request, 'flikcr_api/editePresets.html', context)
