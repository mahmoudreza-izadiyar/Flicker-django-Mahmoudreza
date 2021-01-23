from django.shortcuts import render
from .models import Preset, FavouritePlaces
from .forms import PresetForm


# Create your views here.

def index(request):
    presets = Preset.objects.all()

    if request.method == 'POST':
        cityid = request.POST.get('city')
        city = Preset.objects.get(id=cityid)
        print(city.longitude)
        print(city.latitude)
    else:
        city = ""

    context = {

        "city": city,
        "presets": presets,
    }
    return render(request, 'flikcr_api/index.html', context)


def searchLatLon(request):
    if request.method == 'POST':
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
    else:
        longitude = ""
        latitude = ""

    context = {
        "longitude": longitude,
        "latitude": latitude,

    }
    return render(request, 'flikcr_api/searchLatLon.html', context)


def favourites(request):
    favourites = FavouritePlaces.objects.all()
    context = {
        "favourites": favourites,
    }
    return render(request, 'flikcr_api/fav.html', context)


def edit(request):
    presets = Preset.objects.all()
    form = PresetForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PresetForm()

    context = {
        "presets": presets,
        "form": form
    }

    return render(request, 'flikcr_api/editePresets.html', context)
