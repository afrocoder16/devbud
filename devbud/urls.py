from django.urls import path, include
from django.contrib import admin  # Add this import
from . import views
from accounts.views import public_feed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', public_feed, name='home'),  # ✅ Home page
    path('accounts/', include('accounts.urls')),
    path('projects/', include('projects.urls')),  # ✅ Include projects URLs
    path('messages/', include('messaging.urls')),  # ✅ Include messages URLs
    path('community/', include('community.urls')),  # ✅ Include community URLs

]