from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player, Tag
from django.db.models import Q
from .forms import PlayerForm
from django.contrib.auth.decorators import login_required
from .utils import searchPlayers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def players(request):
    players, search_query = searchPlayers(request)
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(players, results)
    profile = request.user.profile

    try:
        players = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        players = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        players = paginator.page(page)

    context = {
        "players": players,
        "search_query": search_query,
        "profile": profile,
        'paginator': paginator
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
