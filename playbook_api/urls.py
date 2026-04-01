from django.urls import path
from . import views

urlpatterns = [
    path('games/nhl', views.nhl_games),
    path('games/mlb', views.mlb_games),
    path('games/nba', views.nba_games)
]