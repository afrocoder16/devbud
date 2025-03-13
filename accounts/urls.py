from django.urls import path
from .views import (
    ProfileListView,
    ProfileDetailView,
    ProfileCreateView,
    ProfileUpdateView,
    ProfileDeleteView,
)

urlpatterns = [
    path('profiles/', ProfileListView.as_view(), name='profile_list'),
    path('profiles/create/', ProfileCreateView.as_view(), name='profile_create'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profiles/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profiles/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
]
