from django.shortcuts import render
from django.http import HttpResponse
from .models import Player




def players(request):
    players = Player.objects.all()
    context = {"players": players}
    return render(request, "first_project/projects.html", context)


def player(request, pk):
    playerObj = Player.objects.get(id=pk)
    return render(request, "first_project/single-project.html", {"player": playerObj})

def CreateTeam(request):
    context = {}
    return render(request, "first_project/project_form.html", context)