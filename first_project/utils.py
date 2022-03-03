from .models import Player, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def pagination_project(request, players, results_on_page):
    page = request.GET.get("page")
    paginator = Paginator(players, results_on_page)

    try:
        players = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        players = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        players = paginator.page(page)

    left_index = int(page) - 2
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 3
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, players


def search_players(request):
    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    tags = Tag.objects.filter(name__icontains=search_query)
    players = Player.objects.distinct().filter(
        Q(title__icontains=search_query)
        | Q(description__icontains=search_query)
        | Q(owner__name__icontains=search_query)
        | Q(tags__in=tags)
    )
    return players, search_query
