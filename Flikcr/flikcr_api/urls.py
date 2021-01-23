from django.urls import path

from . import views

urlpatterns = [

    path('searchPresets/', views.index, name='searchPresets'),
    path('searchLatLon/', views.searchLatLon, name='searchLatLon'),
    path('favourites/', views.favourites, name='fav'),
    path('editPreset/', views.edit, name='edit'),

]
