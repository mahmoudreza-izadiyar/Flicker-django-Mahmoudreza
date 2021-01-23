from django.urls import path

from . import views

urlpatterns = [

    path('index/', views.index, name='index'),
    path('favourites/', views.favourites, name='fav'),
    path('editPreset/', views.edit, name='edit'),

]
