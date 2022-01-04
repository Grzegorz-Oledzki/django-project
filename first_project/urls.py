from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.players, name='players'),
    path('player/<str:pk>', views.player, name='player')
]