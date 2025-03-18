from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# ✅ User Registration Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# ✅ User Profile Form
class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, label="First Name")
    last_name = forms.CharField(max_length=30, required=False, label="Last Name")
    email = forms.EmailField(required=False, label="Email")

    class Meta:
        model = Profile
        fields = [
            'date_of_birth',
            'location',
            'profile_picture',
            'linkedin',
            'github',
            'website',
            'experience_level',
            'interests',
            'bio',
            'skills',
            'mentor',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # If the instance has an associated user, populate user fields
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

        # Add placeholder text for better UX
        for field in self.fields:
            if field not in ['mentor', 'profile_picture']:
                self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': f'Enter {field.replace("_", " ")}'})

    def save(self, commit=True):
        profile = super().save(commit=False)
        
        # Update user model fields
        if profile.user:
            user = profile.user
            user.first_name = self.cleaned_data.get('first_name', user.first_name)
            user.last_name = self.cleaned_data.get('last_name', user.last_name)
            user.email = self.cleaned_data.get('email', user.email)

            if commit:
                user.save()

        if commit:
            profile.save()

        return profile
