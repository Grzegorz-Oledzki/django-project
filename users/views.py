from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.models import Profile, Skill
from django.contrib.auth.models import User
from django.contrib import messages
from users.models import Profile, Skill, Message
from users.forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from django.contrib.auth.decorators import login_required
from users.utils import search_profiles, pagination_project, unread_message


def login_user(request):
    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]

        try:
            User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET["next"] if "next" in request.GET else "account")
        else:
            messages.error(request, "Username or password is incorrect")

    return render(request, "users/login_register.html")


def logout_user(request):
    logout(request)
    messages.success(request, "User logout!")
    return redirect("login")


def register_user(request):
    page = "register"
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User registered!")
            login(request, user)
            return redirect("edit-account")

        else:
            messages.error(request, "Error! User not registered")

    context = {"page": page, "form": form}
    return render(request, "users/login_register.html", context)


def profiles(request):
    profiles, search_query = search_profiles(request)
    results_on_page = 6
    custom_range, profiles = pagination_project(request, profiles, results_on_page)
    context = {
        "profiles": profiles,
        "custom_range": custom_range,
        "search_query": search_query,
    }
    unread_message(request, context)
    return render(request, "users/profiles.html", context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")
    context = {
        "profile": profile,
        "top_skills": top_skills,
        "other_skills": other_skills,
    }
    unread_message(request, context)
    return render(request, "users/user-profile.html", context)


@login_required(login_url="login")
def user_account(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    players = profile.player_set.all()
    context = {"profile": profile, "skills": skills, "players": players}
    unread_message(request, context)
    return render(request, "users/account.html", context)


@login_required(login_url="login")
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "User edited!")

            return redirect("account")
    context = {"form": form}
    unread_message(request, context)
    return render(request, "users/profile_form.html", context)


@login_required(login_url="login")
def create_skill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "Skill created")
            return redirect("account")
    context = {"form": form}
    unread_message(request, context)
    return render(request, "users/skill_form.html", context)


@login_required(login_url="login")
def update_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill updated")
            return redirect("account")
    context = {"form": form}
    unread_message(request, context)
    return render(request, "users/skill_form.html", context)


@login_required(login_url="login")
def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill deleted")
        return redirect("account")
    context = {"skill": skill}
    unread_message(request, context)
    return render(request, "users/delete_skill.html", context)


@login_required(login_url="login")
def inbox(request):
    profile = request.user.profile
    message_request = profile.messages.all()
    unread_count = message_request.filter(is_read=False).count()
    context = {"message_request": message_request, "unread_count": unread_count}
    return render(request, "users/inbox.html", context)


@login_required(login_url="login")
def view_message(request, pk):
    profile = request.user.profile
    message_request = profile.messages.all()
    this_message = profile.messages.get(id=pk)
    sender = this_message.sender
    sender_message_request = sender.messages.all()

    if not this_message.is_read:
        this_message.is_read = True
        this_message.save()
    context = {"profile": profile, "this_message": this_message, "sender": sender, "message_request": message_request, "sender_message_request": sender_message_request}
    unread_message(request, context)
    return render(request, "users/message.html", context)


@login_required(login_url="login")
def send_message(request, pk):
    sender = request.user.profile
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.sender_name = sender
            message.recipient = recipient
            message.save()
            messages.success(request, "Message sent")
            return redirect("user-profile", pk=recipient.id)
    context = {"form": form, "recipient": recipient, "sender": sender}
    unread_message(request, context)
    return render(request, "users/message_form.html", context)


@login_required(login_url="login")
def delete_message(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if request.method == "POST":
        message.delete()
        messages.success(request, "Message deleted")
        return redirect("inbox")
    context = {"profile": profile, "message": message}
    unread_message(request, context)
    return render(request, "users/delete_message.html", context)
