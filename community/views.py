from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Group, Event, Hackathon, Job, LearningResource, ProgressTracking, CommunityPost, CommunityPost
from .forms import GroupForm, EventForm, HackathonForm, JobForm, LearningResourceForm, ProgressTrackingForm, CommentForm, CommunityPostForm 
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, CreateView

# Group Views
class GroupListView(ListView):
    model = Group
    template_name = 'community/group_list.html'
    context_object_name = 'groups'

class GroupDetailView(DetailView):
    model = Group
    template_name = 'community/group_detail.html'
    context_object_name = 'group'

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'community/group_form.html'
    success_url = reverse_lazy('group_list')

class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'community/group_form.html'
    success_url = reverse_lazy('group_list')

class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'community/group_confirm_delete.html'
    success_url = reverse_lazy('group_list')

# Event Views
class EventListView(ListView):
    model = Event
    template_name = 'community/event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'community/event_detail.html'
    context_object_name = 'event'

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'community/event_form.html'
    success_url = reverse_lazy('event_list')

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'community/event_form.html'
    success_url = reverse_lazy('event_list')

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'community/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')

# Hackathon Views
class HackathonListView(ListView):
    model = Hackathon
    template_name = 'community/hackathon_list.html'
    context_object_name = 'hackathons'

class HackathonDetailView(DetailView):
    model = Hackathon
    template_name = 'community/hackathon_detail.html'
    context_object_name = 'hackathon'

class HackathonCreateView(LoginRequiredMixin, CreateView):
    model = Hackathon
    form_class = HackathonForm
    template_name = 'community/hackathon_form.html'
    success_url = reverse_lazy('hackathon_list')

class HackathonUpdateView(LoginRequiredMixin, UpdateView):
    model = Hackathon
    form_class = HackathonForm
    template_name = 'community/hackathon_form.html'
    success_url = reverse_lazy('hackathon_list')

class HackathonDeleteView(LoginRequiredMixin, DeleteView):
    model = Hackathon
    template_name = 'community/hackathon_confirm_delete.html'
    success_url = reverse_lazy('hackathon_list')

# Job Views
class JobListView(ListView):
    model = Job
    template_name = 'community/job_list.html'
    context_object_name = 'jobs'

class JobDetailView(DetailView):
    model = Job
    template_name = 'community/job_detail.html'
    context_object_name = 'job'

class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'community/job_form.html'
    success_url = reverse_lazy('job_list')

class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'community/job_form.html'
    success_url = reverse_lazy('job_list')

class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Job
    template_name = 'community/job_confirm_delete.html'
    success_url = reverse_lazy('job_list')

# Learning Resource Views
class LearningResourceListView(ListView):
    model = LearningResource
    template_name = 'community/resource_list.html'
    context_object_name = 'resources'

    def get_queryset(self):
        queryset = LearningResource.objects.all().order_by('-posted_at')
        search = self.request.GET.get('search')
        tag = self.request.GET.get('tag')

        if search:
            queryset = queryset.filter(title__icontains=search)

        if tag:
            queryset = queryset.filter(tags__icontains=tag)

        return queryset


class LearningResourceDetailView(DetailView):
    model = LearningResource
    template_name = 'community/resource_detail.html'
    context_object_name = 'resource'

class LearningResourceCreateView(LoginRequiredMixin, CreateView):
    model = LearningResource
    form_class = LearningResourceForm
    template_name = 'community/resource_form.html'
    success_url = reverse_lazy('resource_list')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user  # ✅ Set the user
        return super().form_valid(form)

class LearningResourceUpdateView(LoginRequiredMixin, UpdateView):
    model = LearningResource
    form_class = LearningResourceForm
    template_name = 'community/resource_form.html'
    success_url = reverse_lazy('resource_list')

class LearningResourceDeleteView(LoginRequiredMixin, DeleteView):
    model = LearningResource
    template_name = 'community/resource_confirm_delete.html'
    success_url = reverse_lazy('resource_list')

# Progress Tracking Views
class ProgressTrackingListView(ListView):
    model = ProgressTracking
    template_name = 'community/progress_list.html'
    context_object_name = 'progresses'

class ProgressTrackingDetailView(DetailView):
    model = ProgressTracking
    template_name = 'community/progress_detail.html'
    context_object_name = 'progress'

class ProgressTrackingCreateView(LoginRequiredMixin, CreateView):
    model = ProgressTracking
    form_class = ProgressTrackingForm
    template_name = 'community/progress_form.html'
    success_url = reverse_lazy('progress_list')

class ProgressTrackingUpdateView(LoginRequiredMixin, UpdateView):
    model = ProgressTracking
    form_class = ProgressTrackingForm
    template_name = 'community/progress_form.html'
    success_url = reverse_lazy('progress_list')

class ProgressTrackingDeleteView(LoginRequiredMixin, DeleteView):
    model = ProgressTracking
    template_name = 'community/progress_confirm_delete.html'
    success_url = reverse_lazy('progress_list')

class CommunityFeedView(ListView):
    model = CommunityPost
    template_name = 'community/community_feed.html'  
    context_object_name = 'posts'

    def get_queryset(self):
        return CommunityPost.objects.order_by('-created_at')  
    
class CommunityPostDetailView(FormMixin, DetailView):
    model = CommunityPost
    template_name = 'community/community_post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self):
        return self.request.path

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = self.object
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

@login_required
def like_post(request, pk):
    post = get_object_or_404(CommunityPost, pk=pk)
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', pk=pk)

@login_required
def dislike_post(request, pk):
    post = get_object_or_404(CommunityPost, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
    return redirect('post_detail', pk=pk)

class CommunityPostCreateView(LoginRequiredMixin, CreateView):
    model = CommunityPost
    form_class = CommunityPostForm  # ✅ use your custom form
    template_name = 'community/community_post_form.html'
    success_url = reverse_lazy('community_feed')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
@login_required
def join_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.members.add(request.user)
    return redirect('group_detail', pk=pk)

@login_required
def leave_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.members.remove(request.user)
    return redirect('group_detail', pk=pk)