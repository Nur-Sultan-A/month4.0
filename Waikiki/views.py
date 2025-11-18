from django.shortcuts import render
from . import models


#Все товары
def all_thingsView(request):
    if request.method == 'GET':
        things = models.Products.objects.all()
        return render(request, 'waikiki/all_things.html', {'things': things})

#Домашняя одежда
def homeThingsView(request):
    if request.method == 'GET':
        home_things = models.Products.objects.filter(tags__name='#Домашняя одежда')
        return render(request, 'waikiki/home_things.html', {'home_things':home_things})

#Аксессуары
def accessoriesView(request):
    if request.method == 'GET':
        accessories = models.Products.objects.filter(tags__name='#Аксессуары')
        return render(request, 'waikiki/accessories.html', {'accessories':accessories})

#Обувь
def shoesView(request):
    if request.method == 'GET':
        shoes = models.Products.objects.filter(tags__name='#Обувь')
        return render(request, 'waikiki/shoes.html', {'shoes':shoes})

#Платья
def dressView(request):
    if request.method == 'GET':
        dress = models.Products.objects.filter(tags__name='#Платья')
        return render(request, 'waikiki/dress.html', {'dress':dress})

#Верхняя одежда
def outerwearView(request):
    if request.method == 'GET':
        outerwear = models.Products.objects.filter(tags__name='#Верхняя одежда')
        return render(request, 'waikiki/outerwear.html', {'outerwear':outerwear})