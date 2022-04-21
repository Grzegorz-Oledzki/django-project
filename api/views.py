from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from api.serializers import PlayerSerializer
from first_project.models import Player, Review, Tag


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


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def project_vote(request, pk):
    player = Player.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    review, created = Review.objects.get_or_create(owner=user, player=player)

    review.value = data["value"]
    review.save()
    player.get_vote_count
    serializer = PlayerSerializer(player, many=False)
    return Response(serializer.data)


@api_view(["DELETE"])
def remove_tag(request):
    tagId = request.data["tag"]
    playerId = request.data["player"]
    player = Player.objects.get(id=playerId)
    tag = Tag.objects.get(id=tagId)
    player.tags.remove(tag)
    return Response("Tag was deleted")
