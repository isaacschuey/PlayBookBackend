import requests
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

"""
Game API endpoints
"""
@api_view(['GET'])
def mlb_games(req: Request) -> Response:
    date = req.query_params.get("date")
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&hydrate=team,stats,game,venue&language=en&date={date}"
    response = requests.get(url)
    return Response(response.json())

@api_view(['GET'])
def nba_games(req: Request) -> Response:
    url = "https://cdn.nba.com/static/json/staticData/scheduleLeagueV2_1.json"
    response = requests.get(url)
    return Response(response.json())

@api_view(['GET'])
def nhl_games(req: Request) -> Response:
    date = req.query_params.get("date")
    url = f"https://api-web.nhle.com/v1/score/{date}"
    response = requests.get(url)
    return Response(response.json())

"""
Player API endpoints
"""
@api_view(['GET'])
def mlb_players_hitting(req: Request) -> Response:
    url = "https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?season=2026&stats=season&group=hitting&limit=100&offset=0&sortStat=homeRuns"
    response = requests.get(url)
    return Response(response.json())

@api_view(['GET'])
def mlb_players_pitching(req: Request) -> Response:
    url = "https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?season=2026&stats=season&group=pitching&limit=100&offset=0&sortStat=strikeouts"
    response = requests.get(url)
    return Response(response.json())

@api_view(['GET'])
def nba_players(req: Request) -> Response:
    url = "https://stats.nba.com/stats/leaguedashplayerstats?LeagueID=00&MeasureType=Base&PerMode=Totals&Season=2025-26&SeasonType=Regular%20Season&LastNGames=0&Month=0&OpponentTeamID=0&PORound=0&Period=0&TeamID=0&PaceAdjust=N&PlusMinus=N&Rank=N"
    headers = {
        "Referer": "https://www.nba.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    }
    response = requests.get(url, headers=headers)
    return Response(response.json())

@api_view(['GET'])
def nhl_players(req: Request) -> Response:
    url = "https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22gamesPlayed%22,%22direction%22:%22ASC%22%7D,%7B%22property%22:%22playerId%22,%22direction%22:%22ASC%22%7D%5D&start=0&limit=50&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20252026%20and%20seasonId%3E=20252026"
    response = requests.get(url)
    return Response(response.json())
