from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required  
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile
from .forms import ProfileForm, RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

# ✅ User Registration
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # (Signal auto-creates the profile, so no need to manually create one)
            login(request, user)
            return redirect('user_home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


# ✅ User Home (Redirects to Feed)
@login_required
def user_home(request):
    return render(request, 'feed/feed.html', {'user': request.user})


# ✅ Account Settings (Additional Settings Page)
@login_required
def account_settings(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('account_profile', pk=request.user.profile.pk)
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/account_settings.html', {'form': form})


# ✅ Profile Views (Class-Based)

class ProfileListView(ListView):
    model = Profile
    template_name = 'accounts/home.html'
    context_object_name = 'profiles'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        user_id = self.kwargs.get('pk')
        profile = Profile.objects.filter(user__id=user_id).first()
        if not profile:
            raise Http404("No Profile found for this user")
        return profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_form.html'
    success_url = reverse_lazy('user_home')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_edit.html'  # Uses profile_edit.html

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)

    def form_valid(self, form):
        self.object = form.save()
        return redirect('account_profile', pk=self.request.user.profile.pk)


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile_confirm_delete.html'
    success_url = reverse_lazy('user_home')


# ✅ Public Feed (For Non-Logged-In Users)
def public_feed(request):
    return render(request, 'feed/public_feed.html')
