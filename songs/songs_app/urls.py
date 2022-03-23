from django.urls import path
from . import views

urlpatterns = [
    path("performance/", views.performance_list),
    path("songs/", views.songs_list),
    path("artists/", views.artist_list),
    path("user/", views.user_list),
    path("reviews/", views.reviews_list),
    path("songs/<int:pk>", views.song_details),
    path("artists/<int:pk>", views.artist_details),
    path("performance/<int:pk>", views.performance_details),
    path("reviews/<int:pk>", views.review_details),
    path("user/<int:pk>", views.user_details)
]