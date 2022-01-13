from django.urls import path
from . import views

urlpatterns = [
    path('', views.players, name='players'),
    path('player/<str:pk>/', views.player, name='player'),
    path('create-player/', views.createPlayer, name='create-player'),
    path('update-player/<str:pk>/', views.updatePlayer, name='update-player'),
    path('delete-player/<str:pk>/', views.deletePlayer, name='delete-player'),

]
