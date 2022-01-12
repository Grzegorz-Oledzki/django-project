from django.shortcuts import render
from django.http import HttpResponse
from .models import Player

projectsList = [
    {"id": "1", "name": "Edin Dzeko", "description": "Tall striker"},
    {"id": "2", "name": "Lautaro Martinez", "description": "Effective striker"},
    {"id": "3", "name": "Nicolo Barella", "description": "Clever midfielder"},
]


def players(request):
    players = Player.objects.all()
    context = {"players": players}
    return render(request, "first_project/projects.html", context)


def player(request, pk):
    playerObj = Player.objects.get(id=pk)
    tags = playerObj.tags.all()
    print('playerObj:', playerObj)
    return render(request, "first_project/single-project.html", {"player": playerObj, 'tags': tags})
