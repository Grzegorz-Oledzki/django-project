from django.shortcuts import render
from .models import Profile, Skill


def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, "users/profiles.html", context)
