from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required  # ✅ Add this import
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile
from .forms import ProfileForm, RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # ✅ Create a Profile automatically for the new user
            Profile.objects.create(user=user)  
            login(request, user)
            return redirect('account_profile', pk=user.pk)  # ✅ Redirect using correct user ID
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'accounts/user_home.html', {'user': request.user})

@login_required
def profile(request, pk):
    user_profile = get_object_or_404(Profile, user__pk=pk)  # ✅ Get user profile
    return render(request, 'accounts/profile.html', {'profile': user_profile})

@login_required
def account_settings(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('account_profile', pk=request.user.pk)  # ✅ Redirect to profile after saving
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'accounts/account_settings.html', {'form': form})


class ProfileListView(ListView):
    model = Profile
    template_name = 'accounts/home.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_form.html'
    success_url = reverse_lazy('home')

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_form.html'
    success_url = reverse_lazy('home')

class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'accounts/profile_confirm_delete.html'
    success_url = reverse_lazy('home')

def public_feed(request):
    return render(request, 'feed/public_feed.html')

