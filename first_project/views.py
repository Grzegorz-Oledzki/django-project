from django.shortcuts import render
from django.http import HttpResponse
projectsList = [
    {
        'id': '1',
        'name': 'Edin Dzeko',
        'description': 'Tall striker'
    },
    {
        'id': '2',
        'name': 'Lautaro Martinez',
        'description': 'Effective striker'
    },
    {
        'id': '3',
        'name': 'Nicolo Barella',
        'description': 'Clever midfielder'
    }
]


def players(request):
    page = "players"
    number = 10
    context = {'page': page, 'number': number, 'players': projectsList}
    return render(request, 'first_project/projects.html', context)

def player(request, pk):
    playerObj = None
    for i in projectsList:
        if i['id'] == pk:
            playerObj = i
    return render(request, 'first_project/single-project.html', {'player': playerObj})

