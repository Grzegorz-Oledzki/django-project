from django.urls import path
from . import views

urlpatterns = [
    path("", views.players, name="players"),
    path("player/<str:pk>", views.player, name="player"),
    path('create-player', views.CreatePlayer, name='create-player')
]
