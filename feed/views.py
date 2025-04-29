from django.shortcuts import render
from django.utils import timezone

from projects.models import Project
from community.models import Event, Hackathon, CommunityPost

def home(request):
    # 1) Trending Projects (latest 10)
    trending_projects = Project.objects.order_by('-created_at')[:10]
    
    # 2) Upcoming Events (next 5)
    upcoming_events = (
        Event.objects
             .filter(event_date__gte=timezone.now())
             .order_by('event_date')[:5]
    )
    
    # 3) Active Hackathons (still open)
    active_hackathons = (
        Hackathon.objects
                 .filter(submission_deadline__gte=timezone.now())
                 .order_by('submission_deadline')[:5]
    )
    
    # 4) Recent Community Posts (latest 10)
    recent_posts = CommunityPost.objects.order_by('-created_at')[:10]
    
    return render(request, 'home.html', {
        'projects': trending_projects,
        'events': upcoming_events,
        'hackathons': active_hackathons,
        'posts': recent_posts,
    })
