from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me_view, name='about_me'),
    path('authors/', views.authors_random_view, name='authors'),
    path('time/', views.time_view, name='time'),
]