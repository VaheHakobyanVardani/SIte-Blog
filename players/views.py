from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import  *
from django.db.models import F
# Create your views here.


def Players(request):
    return render(request, 'players/players.html')

class Players(ListView):
        model = Player
        template_name = 'players/players.html'
        context_object_name = 'players'
        paginate_by = 6
        allow_empty = False

        def get_context_data(self,*,object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            return context

class GetSinglePlayer(DetailView):
    model = Player
    template_name = 'players/single_player.html'
    context_object_name = 'player'

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
