from django.shortcuts import render
from django.http import HttpResponse

def players(request):
    return HttpResponse('Here are out players')

def player(request, pk):
    return HttpResponse('Here are out player' + ' ' + str(pk))

