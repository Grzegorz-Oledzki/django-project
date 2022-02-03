from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player
from .forms import PlayerForm
from django.contrib.auth.decorators import login_required



def players(request):
    players = Player.objects.all()
    context = {"players": players}
    return render(request, "first_project/projects.html", context)


def player(request, pk):
    playerObj = Player.objects.get(id=pk)
    return render(request, "first_project/single-project.html", {"player": playerObj})

@login_required(login_url='login')
def createPlayer(request):
    form = PlayerForm()

    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("players")

    context = {"form": form}
    return render(request, "first_project/project_form.html", context)

@login_required(login_url='login')
def updatePlayer(request, pk):
    player = Player.objects.get(id=pk)
    form = PlayerForm(instance=player)

    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect("players")

    context = {"form": form}
    return render(request, "first_project/project_form.html", context)

@login_required(login_url='login')
def deletePlayer(request, pk):
    player = Player.objects.get(id=pk)
    context = {"player": player}
    if request.method == "POST":
        player.delete()
        return redirect("players")
    return render(request, "first_project/delete_obj.html", context)
