from urllib import request

from django.shortcuts import render
from apps.bookmodule.models import Game

def index(request):
    return render(request, "bookmodule/index.html")

def list_games(request):
    return render(request, 'bookmodule/list_games.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def viewgame(request, gameId):
    
    game_id_str = str(gameId)
    
    if game_id_str == "1":
        return render(request, 'bookmodule/hollow_knight.html')
    elif game_id_str == "2":
        return render(request, 'bookmodule/baldurs_gate.html')
    elif game_id_str == "3":
        return render(request, 'bookmodule/yakuza0.html')
    else:
        return render(request, 'bookmodule/list_games.html')
def list_games(request):
    my_games = Game.objects.all()
    return render(request, 'bookmodule/list_games.html', {'games': my_games})

def lab5_query(request):
    my_games = Game.objects.filter(price__gt=10).filter(title__icontains='Hollow')
    return render(request, 'bookmodule/list_games.html', {'games': my_games})

def links_view(request):
    return render(request, 'bookmodule/links.html')

def listing_view(request):
    return render(request, 'bookmodule/listing.html')

def tables_view(request):
    return render(request, 'bookmodule/tables.html')

def formatting_view(request):
    return render(request, 'bookmodule/formatting.html')
