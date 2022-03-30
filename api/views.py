from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import PlayerSerializer
from first_project.models import Player


@api_view(["GET"])
def get_routes(request):
    routes = [
        {"GET": "/api/players"},
        {"GET": "/api/players/id"},
        {"POST": "/api/players/id/vote"},
        {"POST": "/api/user/token"},
        {"POST": "/api/user/token/refresh"},
    ]
    return Response(routes)


@api_view(["GET"])
def get_players(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_player(request, pk):
    players = Player.objects.get(id=pk)
    serializer = PlayerSerializer(players, many=False)
    return Response(serializer.data)
