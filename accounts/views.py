from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required  
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile
from .forms import ProfileForm, RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Ensure Profile is created
            profile, created = Profile.objects.get_or_create(user=user)

            login(request, user)
            return redirect('user_home')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})



@login_required
def user_home(request):
    return render(request, 'feed/feed.html', {'user': request.user})  # Updated to feed.html


@login_required
def profile(request, pk):
    user_profile = get_object_or_404(Profile, user__pk=pk)
    return render(request, 'accounts/profile.html', {'profile': user_profile})


@login_required
def account_settings(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account_profile', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/account_settings.html', {'form': form})


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
        profile = Profile.objects.filter(user_id=user_id).first()
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
    template_name = 'accounts/profile_edit.html'

    def get_object(self, queryset=None):
        user_profile = Profile.objects.filter(user=self.request.user).first()
        if not user_profile:
            print(f"❌ Profile not found for user: {self.request.user.username}")
        else:
            print(f"✅ Profile found for user: {self.request.user.username}")
        return user_profile

    def form_valid(self, form):
        print(f"📝 Form is valid. Updating profile for user: {self.request.user.username}")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(f"❌ Form is invalid. Errors: {form.errors}")
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy('account_profile', kwargs={'pk': self.request.user.profile.pk})


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile_confirm_delete.html'
    success_url = reverse_lazy('user_home')


def public_feed(request):
    return render(request, 'feed/public_feed.html')
