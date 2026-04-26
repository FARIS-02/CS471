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

    path('lab8/task1', views.task1, name="games.task1"),
    path('lab8/task2', views.task2, name="games.task2"),
    path('lab8/task3', views.task3, name="games.task3"),
    path('lab8/task4', views.task4, name="games.task4"),
    path('lab8/task5', views.task5, name="games.task5"),
    path('lab8/task7', views.task7, name="games.task7"),

    path('lab9/task1', views.task1, name="lab9.task1"),
    path('lab9/task2', views.task2, name="lab9.task2"),
    path('lab9/task3', views.task3, name="lab9.task3"),
    path('lab9/task4', views.task4, name="lab9.task4"),
    path('lab9/task5', views.task5, name="lab9.task5"),
    path('lab9/task6', views.task6, name="lab9.task6"),
]