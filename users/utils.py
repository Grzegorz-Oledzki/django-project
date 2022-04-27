from .models import Profile, Skill
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

    left_index = int(page) - 1
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 2
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, players


def search_profiles(request):
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    skills = Skill.objects.filter(name__iexact=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query)
        | Q(username__icontains=search_query)
        | Q(skill__in=skills)
        | Q(location__icontains=search_query)
    )

    return profiles, search_query


def unread_message(request, context):
    if request.user.is_authenticated:
        profile = request.user.profile
        message_request = profile.messages.all()
        unread_count = message_request.filter(is_read=False).count()
        context["unread_count"] = unread_count