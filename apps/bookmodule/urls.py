from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="games.index"),
    path('list_books/', views.list_games, name="games.list_games"),
    path('aboutus/', views.aboutus, name="games.aboutus"),
    path('<int:gameId>/', views.viewgame, name="games.view_one_game"),
    path('html5/links/', views.links_view, name="games.links"),
    path('html5/listing/', views.listing_view, name="games.listing"),
    path('html5/tables/', views.tables_view, name="games.tables"),
    path('html5/text/formatting/', views.formatting_view, name="games.formatting"),
    path('search', views.search_view, name="books.search"),
    path('search', views.search_view, name="games.search"),
    path('simple/query', views.simple_query, name="games.simple_query"),
    path('complex/query', views.complex_query, name="games.complex_query"),
]