from django.urls import path
from . import views

urlpatterns = [
    path("", views.players, name="players"),
    path("player/<str:pk>/", views.player, name="player"),
    path("create-player/", views.create_player, name="create-player"),
    path("update-player/<str:pk>/", views.update_player, name="update-player"),
    path("delete-player/<str:pk>/", views.delete_player, name="delete-player"),
]
