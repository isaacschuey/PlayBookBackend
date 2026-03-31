from django.urls import path
from . import views

urlpatterns = [
    path('hockey/<str:date>/', views.hockey_games),
]