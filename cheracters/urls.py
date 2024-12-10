from django.urls import path
from rest_framework.urls import app_name

from cheracters.views import get_random_characters_views, CharacterListView

app_name = "characters"

urlpatterns = [
    path("characters/random", get_random_characters_views, name="character-random"),
    path("characters/", CharacterListView.as_view(), name="character-list"),
]
