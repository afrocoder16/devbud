from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Public feed (for non-logged-in users)
def public_feed(request):
    return render(request, 'feed/feed.html', {'user': request.user, 'public': True})

# Personalized feed (for logged-in users)
@login_required
def personalized_feed(request):
    return render(request, 'feed/feed.html', {'user': request.user, 'public': False})
