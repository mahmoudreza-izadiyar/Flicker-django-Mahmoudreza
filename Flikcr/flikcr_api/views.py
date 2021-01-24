from django.shortcuts import render
import flickrapi
from .models import Preset, FavouritePlaces
from .forms import PresetForm

api_key = "02df6aacd6e20bed557b78d7dc1d143a"
secret_api_key = "5a2087a02ab2540c"
flickr = flickrapi.FlickrAPI(api_key, secret_api_key)

# Search function
def search(lat, lon):
    # Calling Flickr API and Create Photos object
    obj = flickr.photos.search(api_key=api_key, lat=lat, lon=lon, accuracy=11, format='parsed-json')
    photos = obj['photos']['photo']

    # Create photo addresses
    adresses = []
    for photo in photos:
        farm_id = photo['farm']
        server_id = photo['server']
        id = photo['id']
        secret = photo['secret']
        address = f"https://farm{farm_id}.staticflickr.com/{server_id}/{id}_{secret}.jpg"
        adresses.append(address)
    return adresses


# Search photos with presets
def index(request):
    presets = Preset.objects.all()
    cityid = ""
    addresses = ""

    if request.method == 'POST':
        presets = Preset.objects.all()
        cityname = request.POST.get('city')
        cityid = Preset.objects.get(id=cityname)
        lat = cityid.latitude
        lon = cityid.longitude
        addresses = search(lat, lon)
        print(cityid.longitude)
        print(cityid.latitude)
        print(addresses)




    context = {
        'addresses': addresses,
        "city": cityid,
        "presets": presets,
    }
    return render(request, 'flikcr_api/index.html', context)


# search photos with lon and lat
def searchLatLon(request):
    if request.method == 'POST':
        lon = request.POST.get('longitude')
        lat= request.POST.get('latitude')
        addresses = search(lat, lon)

    else:
        lon = ""
        lat = ""
        addresses = ""


    context = {
        'addresses': addresses,
        "longitude": lon,
        "latitude": lat,

    }
    return render(request, 'flikcr_api/searchLatLon.html', context)


# show the Favourite list
def favourites(request):


    context = {

    }
    return render(request, 'flikcr_api/fav.html', context)


# Edite presets in database
def edit(request):
    # Send new object to the model
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
