from django.urls import path
from rest_framework.urls import app_name

from cheracters.views import get_random_characters_views

app_name = "characters"

urlpatterns = [
    path("characters/random", get_random_characters_views, name="get-random"),
]
