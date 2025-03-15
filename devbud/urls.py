from django.urls import path, include
from django.contrib import admin  # Add this import
from . import views
from accounts.views import public_feed

urlpatterns = [
    path('', public_feed, name='home'),  # ✅ Set the public feed as home
    path('feed/', include('feed.urls')),
    path('accounts/', include('accounts.urls')),
    path('projects/', include('projects.urls')),
    path('messaging/', include('messaging.urls')),
    path('community/', include('community.urls')),
]