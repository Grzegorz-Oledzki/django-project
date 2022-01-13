from django.urls import path
from . import views

urlpatterns = [
    path("", views.players, name="players"),
    path("player/<str:pk>", views.player, name="player"),
    path('create-team', views.CreateTeam, name='create-team')
]
