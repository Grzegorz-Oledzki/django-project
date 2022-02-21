from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player, Tag
from django.db.models import Q
from .forms import PlayerForm
from django.contrib.auth.decorators import login_required


def players(request):
    profile = request.user.profile
    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
    players = Player.objects.filter(
        Q(title__icontains=search_query)
        | Q(description__icontains=search_query)
        | Q(owner__name__icontains=search_query)
    )
    tags = Tag.objects.filter(Q(name__icontains=search_query))
    context = {
        "players": players,
        "search_query": search_query,
        "tags": tags,
        "profile": profile,
    }
    return render(request, "first_project/projects.html", context)


def player(request, pk):
    playerObj = Player.objects.get(id=pk)
    return render(request, "first_project/single-project.html", {"player": playerObj})


@login_required(login_url="login")
def createPlayer(request):
    form = PlayerForm()
    profile = request.user.profile
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            player = form.save(commit=False)
            player.owner = profile
            player.save()
            return redirect("account")

    context = {"form": form}
    return render(request, "first_project/project_form.html", context)


@login_required(login_url="login")
def updatePlayer(request, pk):
    profile = request.user.profile
    player = profile.player_set.get(id=pk)
    form = PlayerForm(instance=player)

    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect("account")

    context = {"form": form}
    return render(request, "first_project/project_form.html", context)


@login_required(login_url="login")
def deletePlayer(request, pk):
    player = Player.objects.get(id=pk)
    context = {"player": player}
    if request.method == "POST":
        player.delete()
        return redirect("account")
    return render(request, "first_project/delete_obj.html", context)
