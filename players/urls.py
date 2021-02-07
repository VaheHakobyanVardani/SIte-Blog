from django.urls import path

from .views import *

urlpatterns = [
    path('players/', Players.as_view(), name='players'),
    path('players/<str:slug>/', GetSinglePlayer.as_view(), name='single_player'),
]
