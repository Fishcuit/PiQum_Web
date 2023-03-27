"""
Definition of urls for PiQum_Web.
"""


from django.urls import path

from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('game1/', views.game1, name='game1'),
    path('game2/', views.game2, name='game2'),
    path('game3/', views.game3, name='game3'),
    path('game4/', views.game4, name='game4'),
    
]
