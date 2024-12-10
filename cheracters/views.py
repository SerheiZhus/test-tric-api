import random

from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from cheracters.models import Character
from cheracters.serializers import CharacterSerializer
from pagination import CharacterListPagination


@extend_schema(
    responses={status.HTTP_200_OK: CharacterSerializer},
)
@api_view(["GET"])
def get_random_characters_views(request: Request) -> Response:
    """Return a random character"""
    pks = Character.objects.values_list("pk", flat=True)
    random_pks = random.choice(pks)
    random_characters = Character.objects.get(pk=random_pks)
    serializer = CharacterSerializer(random_characters)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListView(generics.ListAPIView):
    serializer_class = CharacterSerializer
    pagination_class = CharacterListPagination

    def get_queryset(self) -> QuerySet:
        queryset = Character.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="name",
                description="Filter by name insensitive contains",
                required=False,
                type=str,
            ),
        ]
    )
    def get(self, request, *args, **kwargs) -> Response:
        """List characters with optional name filter"""
        return super().get(request, *args, **kwargs)
