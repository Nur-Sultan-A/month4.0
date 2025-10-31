from django.shortcuts import render
from django.http import HttpResponse
import random
from datetime import datetime as dt


def me_view(request):
    if request.method == 'GET':
        return HttpResponse('i guess u dont need to know about me >:)')


def random_view(request):
    if request.method == 'GET':
        blogs_random = ['Чак Паланик', 'Джордж Оруэлл', 'Федор Достоевский', 'Айн Рэнд', 'Артур Конан Дойл']
        return HttpResponse(random.choice(blogs_random))

def time_view(request):
    if request.method == "GET":
        time = dt.now()
        hour = time.strftime("%H")
        if 6 <= int(hour) <= 11:
            return HttpResponse('kofe pey na rabota nada')
        elif 12 <= int(hour) <= 14:
            return HttpResponse('jrat nada')
        elif 15<= int(hour) <= 20:
            return HttpResponse("dotku na paru chasov")
        else:
            return HttpResponse("nado biloo spaat a ne dotu gonat")