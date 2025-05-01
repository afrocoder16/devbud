from django.urls import path
from . import views
from .views import InboxView 

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('conversation/<int:conversation_id>/', views.conversation_detail, name='conversation_detail'),
    path('start/<int:user_id>/', views.start_conversation, name='start_conversation'),
    path('', InboxView.as_view(), name='inbox'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('conversation/<int:pk>/', views.ConversationDetailView.as_view(), name='conversation_detail'),

]

