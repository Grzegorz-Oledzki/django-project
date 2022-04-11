from django.shortcuts import render, redirect
from django.http import HttpResponse
from first_project.models import Player, Tag, Review
from django.db.models import Q
from first_project.forms import PlayerForm, ReviewForm
from django.contrib.auth.decorators import login_required
from first_project.utils import search_players, pagination_project
from django.contrib import messages


def players(request):
    players, search_query = search_players(request)
    results_on_page = 3
    custom_range, players = pagination_project(request, players, results_on_page)

    context = {
        "players": players,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "first_project/projects.html", context)


def player(request, pk):
    playerObj = Player.objects.get(id=pk)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.player = playerObj
        review.owner = request.user.profile
        review.save()
        playerObj.get_vote_count
        messages.success(request, "Review added!")
        return redirect("player", pk=playerObj.id)

    return render(
        request,
        "first_project/single-project.html",
        {"player": playerObj, "form": form},
    )


@login_required(login_url="login")
def create_player(request):
    new_tags = request.POST.get('new_tags').replace(',', ' ').split()
    form = PlayerForm()
    profile = request.user.profile
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            player = form.save(commit=False)
            player.owner = profile
            player.save()
            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                player.tags.add(tag)
            return redirect("account")

    context = {"form": form}
    return render(request, "first_project/project_form.html", context)


@login_required(login_url="login")
def update_player(request, pk):
    profile = request.user.profile
    player = profile.player_set.get(id=pk)
    form = PlayerForm(instance=player)

    if request.method == "POST":
        new_tags = request.POST.get('new_tags').replace(',', ' ').split()
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            player = form.save()
            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                player.tags.add(tag)
            return redirect("account")

    context = {"form": form}
    return render(request, "first_project/project_form.html", context)


@login_required(login_url="login")
def delete_player(request, pk):
    player = Player.objects.get(id=pk)
    context = {"player": player}
    if request.method == "POST":
        player.delete()
        return redirect("account")
    return render(request, "first_project/delete_obj.html", context)
