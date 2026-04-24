from urllib import request

from django.shortcuts import render
from apps.bookmodule.models import Game 
from .models import Game, Player, Address
from django.db.models import Q, Count, Sum, Avg, Max, Min

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

def getGamesList():
    Game1 = {'id': 12344321, 'title': 'Continuous Delivery', 'developer': 'J.Humble and D. Farley'}
    Game2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'developer': 'E. Eilam'}
    Game3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'developer': 'Andriy Burkov'}
    Game4 = {'id': 98765432, 'title': 'final fantasy', 'developer': 'square enix'}  
    Game5 = {'id': 98765432, 'title': 'hollow knight', 'developer': 'team cherry'}  
    Game6 = {'id': 98765432, 'title': 'baldurs gate 3', 'developer': 'loremasters'}
    Game7 = {'id': 98765432, 'title': 'yakuza 0', 'developer': 'sega'}
    Game8 = {'id': 98765432, 'title': 'persona 5', 'developer': 'atlus'}
    Game9 = {'id': 98765432, 'title': 'zelda breath of the wild', 'developer': 'nintendo'}
    Game10 = {'id': 98765432, 'title': 'mario odyssey', 'developer': 'nintendo'}

    return [Game1, Game2, Game3, Game4, Game5, Game6, Game7, Game8, Game9, Game10]

def search_view(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isDeveloper = request.POST.get('option2')
        
        Games = getGamesList()
        newgames = []
        for item in Games:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isDeveloper and string in item['developer'].lower(): contained = True
            
            if contained: newgames.append(item)
        return render(request, 'bookmodule/gamelist.html', {'games': newgames})
    
    return render(request, 'bookmodule/search.html')


def simple_query(request):
    # نبحث عن الألعاب اللي اسمها يحتوي على حرف 'e'
    mygames = Game.objects.filter(title__icontains='e') 
    return render(request, 'bookmodule/list_games.html', {'games': mygames})

def complex_query(request):
    # نبحث عن لعبة لها مطور + اسمها فيه 'e' + سعرها أقل من أو يساوي 50
    mygames = Game.objects.filter(developer__isnull=False).filter(title__icontains='e').exclude(price__gt=50)[:10]
    
    if len(mygames) >= 1:
        return render(request, 'bookmodule/list_games.html', {'games': mygames})
    else:
        return render(request, 'bookmodule/index.html')

def task1(request):
    mygames = Game.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/list_games.html', {'games': mygames})

def task2(request):
    mygames = Game.objects.filter(Q(edition__gt=3) & (Q(title__icontains='qu') | Q(developer__icontains='qu')))
    return render(request, 'bookmodule/list_games.html', {'games': mygames})

def task3(request):
    mygames = Game.objects.filter(~Q(edition__gt=3) & ~(Q(title__icontains='qu') | Q(developer__icontains='qu')))
    return render(request, 'bookmodule/list_games.html', {'games': mygames})

def task4(request):
    mygames = Game.objects.all().order_by('title')
    return render(request, 'bookmodule/list_games.html', {'games': mygames})

def task5(request):
    stats = Game.objects.aggregate(
        total_games=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})

def task7(request):
    cities = Address.objects.annotate(player_count=Count('player'))
    return render(request, 'bookmodule/task7.html', {'cities': cities})

