from django.urls import path, include
from django.contrib import admin
from accounts.views import public_feed
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', public_feed, name='home'),
    path('accounts/', include('accounts.urls')),
    path('projects/', include('projects.urls')),
    path('messaging/', include('messaging.urls')),
    path('community/', include('community.urls')),
    # path('feed/', include('feed.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]

# Append media URL patterns after defining urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
