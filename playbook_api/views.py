import requests
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

@api_view(['GET'])
def mlb_games(req: Request) -> Response:
    date = req.query_params.get("date")
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&hydrate=team,stats,game,venue&language=en&date={date}"
    response = requests.get(url)
    return Response(response.json())

@api_view(['GET'])
def nhl_games(req: Request) -> Response:
    date = req.query_params.get("date")
    url = f"https://api-web.nhle.com/v1/score/{date}"
    response = requests.get(url)
    return Response(response.json())

@api_view(['GET'])
def nba_games(req: Request) -> Response:
    url = "https://cdn.nba.com/static/json/staticData/scheduleLeagueV2_1.json"
    response = requests.get(url)
    return Response(response.json())
