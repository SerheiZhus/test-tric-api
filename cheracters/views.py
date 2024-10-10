import random

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from cheracters.models import Character
from cheracters.serializers import CharacterSerializer


@api_view(["GET"])
def get_random_characters_views(request: Request) -> Response:
    pks = Character.objects.values_list("pk", flat=True)
    random_pks = random.choice(pks)
    random_characters = Character.objects.get(pk=random_pks)
    serializer = CharacterSerializer(random_characters)
    return Response(serializer.data, status=status.HTTP_200_OK)
