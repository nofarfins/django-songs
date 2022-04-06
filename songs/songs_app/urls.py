from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("performance/", views.performance_list),
    path("songs/", views.songs_list),
    path("artists/", views.artist_list),
    path("user/", views.user_list),
    path("reviews/", views.reviews_list),
    path("songs/<int:pk>", views.song_details),
    path("artists/<int:id>", views.artist_details),
    path("performance/<int:pk>", views.performance_details),
    path("performance/<int:performance_id>/review", views.reviews),
    path("reviews/<int:pk>", views.review_details),
    path("user/<int:pk>", views.user_details),
    path("users/current", views.current_user),
    path('token/', obtain_auth_token),
]