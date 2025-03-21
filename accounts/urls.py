from django.urls import path
from django.contrib.auth import views as auth_views  
from django.contrib.auth.views import LogoutView  
from .views import (
    register, 
    account_settings, 
    user_home, 
    profile, 
    public_feed,
    ProfileListView, 
    ProfileDetailView, 
    ProfileCreateView, 
    ProfileUpdateView, 
    ProfileDeleteView
)

urlpatterns = [
    # Authentication Routes
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='account_login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='account_logout'),
    path('register/', register, name='account_register'),

    # Profile Management
    path('profile/<int:pk>/', profile, name='account_profile'),  # View Profile
    path('profile/<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile_edit'),  # Edit Profile
    path('settings/', account_settings, name='account_settings'),  # Account Settings Page

    # User & Profile Listings
    path('profiles/', ProfileListView.as_view(), name='profile_list'),
    path('profiles/create/', ProfileCreateView.as_view(), name='profile_create'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profiles/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profiles/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile_delete'),

    # Home & Feeds
    path('home/', user_home, name='user_home'),  # Personalized Home Page
    path('feed/', public_feed, name='public_feed'),  # Public Feed for non-logged-in users
]
