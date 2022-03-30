from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_routes),
    path("players/", views.get_players),
    path("player/<str:pk>", views.get_player),
]
