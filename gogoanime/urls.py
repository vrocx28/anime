from django.urls import path

from gogoanime import views
from django.conf.urls.static import static

urlpatterns = [
    path('add_anime/', views.add_anime, name='add_anime/'),
    path('anime/', views.all_anime, name='anime/'),
    path('anime/<int:anime_id>/', views.anime_info, name='anime_info/'),
    path('downloadalleps/', views.download_all_eps, name='downloadalleps/'),
]

