from django.urls import path
from .views import (
    GroupListView, GroupDetailView, GroupCreateView, GroupUpdateView, GroupDeleteView,
    EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView,
    HackathonListView, HackathonDetailView, HackathonCreateView, HackathonUpdateView, HackathonDeleteView,
    JobListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView,
    LearningResourceListView, LearningResourceDetailView, LearningResourceCreateView, LearningResourceUpdateView, LearningResourceDeleteView,
    ProgressTrackingListView, ProgressTrackingDetailView, ProgressTrackingCreateView, ProgressTrackingUpdateView, ProgressTrackingDeleteView,
)

urlpatterns = [
    # Groups
    path('groups/', GroupListView.as_view(), name='group_list'),
    path('groups/create/', GroupCreateView.as_view(), name='group_create'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group_detail'),
    path('groups/<int:pk>/update/', GroupUpdateView.as_view(), name='group_update'),
    path('groups/<int:pk>/delete/', GroupDeleteView.as_view(), name='group_delete'),
    
    # Events
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('events/<int:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    
    # Hackathons
    path('hackathons/', HackathonListView.as_view(), name='hackathon_list'),
    path('hackathons/create/', HackathonCreateView.as_view(), name='hackathon_create'),
    path('hackathons/<int:pk>/', HackathonDetailView.as_view(), name='hackathon_detail'),
    path('hackathons/<int:pk>/update/', HackathonUpdateView.as_view(), name='hackathon_update'),
    path('hackathons/<int:pk>/delete/', HackathonDeleteView.as_view(), name='hackathon_delete'),
    
    # Jobs
    path('jobs/', JobListView.as_view(), name='job_list'),
    path('jobs/create/', JobCreateView.as_view(), name='job_create'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('jobs/<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('jobs/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    
    # Learning Resources
    path('resources/', LearningResourceListView.as_view(), name='resource_list'),
    path('resources/create/', LearningResourceCreateView.as_view(), name='resource_create'),
    path('resources/<int:pk>/', LearningResourceDetailView.as_view(), name='resource_detail'),
    path('resources/<int:pk>/update/', LearningResourceUpdateView.as_view(), name='resource_update'),
    path('resources/<int:pk>/delete/', LearningResourceDeleteView.as_view(), name='resource_delete'),
    
    # Progress Tracking
    path('progress/', ProgressTrackingListView.as_view(), name='progress_list'),
    path('progress/create/', ProgressTrackingCreateView.as_view(), name='progress_create'),
    path('progress/<int:pk>/', ProgressTrackingDetailView.as_view(), name='progress_detail'),
    path('progress/<int:pk>/update/', ProgressTrackingUpdateView.as_view(), name='progress_update'),
    path('progress/<int:pk>/delete/', ProgressTrackingDeleteView.as_view(), name='progress_delete'),
]
