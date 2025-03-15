from django.urls import path
from .views import public_feed, personalized_feed

urlpatterns = [
    path('', public_feed, name='public_feed'),  # Public feed at /
    path('feed/', personalized_feed, name='personalized_feed'),  # Personalized feed at /feed/
]
