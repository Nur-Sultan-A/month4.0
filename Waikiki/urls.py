from django.urls import path
from . import views

urlpatterns = [
    path('all_things/', views.all_thingsView, name='all_things'),
    path('home_things/', views.homeThingsView, name='home_things'),
    path('accessories/', views.accessoriesView, name='accessories'),
    path('shoes/', views.shoesView, name='shoes'),
    path('dress/', views.dressView, name='dress'),
    path('outerwear/', views.outerwearView, name='outerwear'),
]