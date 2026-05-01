from datetime import datetime

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
def nba_live_games(req: Request) -> Response:
    url = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"
    response = requests.get(url)
    return Response(response.json())

@api_view(['GET'])
def nba_schedule_games(req: Request) -> Response:
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
    # position url: https://stats.nba.com/stats/playerindex?College=&Country=&DraftPick=&DraftRound=&DraftYear=&Height=&Historical=1&LeagueID=00&Season=2025-26&SeasonType=Regular%20Season&TeamID=0&Weight=
    url = "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&ISTRound=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2025-26&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
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

"""
Team API endpoints
"""
@api_view(['GET'])
def mlb_teams(req: Request) -> Response:
    url = "https://bdfed.stitch.mlbinfra.com/bdfed/transform-mlb-standings?standingsView=division&season=2026&leagueIds=103&leagueIds=104&standingsTypes=regularSeason&date=2026-04-05&sortDivisions=201,202,200,204,205,203&sortLeagues=103,104,115,114&sortSports=1"
    response = requests.get(url)
    return Response(response.json())

@api_view(['GET'])
def nba_teams(req: Request) -> Response:
    url = "https://stats.nba.com/stats/leaguestandingsv3?GroupBy=div&LeagueID=00&Season=2025-26&SeasonType=Regular%20Season&Section=overall"
    headers = {
        "Referer": "https://www.nba.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    }
    response = requests.get(url, headers=headers)
    return Response(response.json())

@api_view(['GET'])
def nhl_teams(req: Request) -> Response:
    # url = f"https://api-web.nhle.com/v1/standings/{datetime.today().strftime('%Y-%m-%d')}"
    url = "https://api-web.nhle.com/v1/standings/2026-04-17" # Standings cutoff for plyoffs - 04/17 is the last day of the regular season
    response = requests.get(url)
    return Response(response.json())