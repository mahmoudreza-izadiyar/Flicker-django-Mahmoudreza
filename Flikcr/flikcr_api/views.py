from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        "name": "mahmoudreza",
    }
    return render(request, 'flikcr_api/index.html', context)
