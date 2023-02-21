from django.urls import path
from . import views

urlpatterns = [ 
    path('alatauskij/', views.houses_alatauskij),
    path('almalinskij/', views.houses_almalinskij),
    path('aujezovskij/', views.houses_aujezovskij),
    path('bostandykskij/', views.houses_bostandykskij),
    path('medeuskij/', views.houses_medeuskij),
    path('nauryzbajskiy/', views.houses_nauryzbajskiy),
    path('turksibskij/', views.houses_turksibskij),
    path('zhetysuskij/', views.houses_zhetysuskij),
    path("analytics/",views.analyzeHouse)
]