from django.urls import path
from . import views

urlpatterns = [
    path('mlb/games', views.mlb_games),
    path('nba/games/live', views.nba_live_games),
    path('nba/games/schedule', views.nba_schedule_games),
    path('nhl/games', views.nhl_games),
    path('mlb/players/hitting', views.mlb_players_hitting),
    path('mlb/players/pitching', views.mlb_players_pitching),
    path('nba/players', views.nba_players),
    path('nhl/players', views.nhl_players)
]