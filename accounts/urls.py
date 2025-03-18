from django.urls import path
from django.contrib.auth import views as auth_views  
from django.contrib.auth.views import LogoutView  
from .views import (
    register, 
    account_settings, 
    user_home, 
    public_feed,
    ProfileListView, 
    ProfileDetailView, 
    ProfileCreateView, 
    ProfileUpdateView, 
    ProfileDeleteView
)

urlpatterns = [
    path('profiles/', ProfileListView.as_view(), name='profile_list'),
    path('profiles/create/', ProfileCreateView.as_view(), name='profile_create'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profiles/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profiles/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='account_login'),
    path('register/', register, name='account_register'),
    path('profile/<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('settings/', account_settings, name='account_settings'),
    path('logout/', LogoutView.as_view(next_page='/'), name='account_logout'),
    path('home/', user_home, name='user_home'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='account_profile'),
    path('feed/', public_feed, name='public_feed'),  # Public feed for non-logged-in users
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='account_profile'),  # Only GET

]
