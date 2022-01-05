from django.shortcuts import render
from django.http import HttpResponse

def players(request):
    return render(request, 'first_project/projects.html')

def player(request, pk):
    return render(request, 'first_project/single-project.html')

