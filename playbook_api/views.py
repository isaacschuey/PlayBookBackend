from django.shortcuts import render

# Create your views here.
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hockey_games(request, date):
    url = f'https://api-web.nhle.com/v1/score/{date}'
    response = requests.get(url)
    return Response(response.json())