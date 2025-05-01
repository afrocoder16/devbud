from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Conversation, Message
from .forms import MessageForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView
from .models import Conversation
from django.views.generic.edit import FormMixin
from django.views.generic.detail import DetailView


@login_required
def inbox(request):
    conversations = request.user.conversations.all()
    return render(request, 'messaging/inbox.html', {'conversations': conversations})

@login_required
def conversation_detail(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    if request.user not in conversation.participants.all():
        return redirect('inbox')
    messages = conversation.messages.order_by('timestamp')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.sender = request.user
            message.save()
            return redirect('conversation_detail', conversation_id=conversation.id)
    else:
        form = MessageForm()
    return render(request, 'messaging/conversation_detail.html', {
        'conversation': conversation,
        'messages': messages,
        'form': form
    })

@login_required
def start_conversation(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    conversation = Conversation.objects.filter(participants=request.user).filter(participants=other_user).first()
    if not conversation:
        conversation = Conversation.objects.create()
        conversation.participants.add(request.user, other_user)
    return redirect('conversation_detail', conversation_id=conversation.id)

class InboxView(LoginRequiredMixin, ListView):
    model = Conversation
    template_name = 'messaging/inbox.html'  # ✅ Create this template next
    context_object_name = 'conversations'

    def get_queryset(self):
        return Conversation.objects.filter(participants=self.request.user)
    
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'messaging/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.exclude(id=self.request.user.id)

class ConversationDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Conversation
    template_name = 'messaging/conversation_detail.html'
    context_object_name = 'conversation'
    form_class = MessageForm

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = self.object.messages.order_by('timestamp')
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.conversation = self.object
            message.save()
            return self.form_valid(form)
        return self.form_invalid(form)