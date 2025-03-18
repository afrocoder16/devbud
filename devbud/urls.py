from django.urls import path, include
from django.contrib import admin  # Add this import
from . import views
from accounts.views import public_feed

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Ensure admin URL is included
    path('', public_feed, name='home'),  # Adjust based on your app structure
    path('accounts/', include('accounts.urls')),
    path('projects/', include('projects.urls')),
    path('messaging/', include('messaging.urls')),
    path('community/', include('community.urls')),
    path('feed/', include('feed.urls')),
]