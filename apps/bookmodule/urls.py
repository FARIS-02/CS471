from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="games.index"),
    path('list_games/', views.list_games, name="games.list_games"),
    path('aboutus/', views.aboutus, name="games.aboutus"),
    path('<int:gameId>/', views.viewgame, name="games.view_one_game"),
    path('html5/links', views.links_view, name="games.links"),
    path('html5/listing', views.listing_view, name="games.listing"),
    path('html5/tables', views.tables_view, name="games.tables"),
]