from django import forms
from .models import Group, Event, Hackathon, Job, LearningResource, ProgressTracking

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description', 'members']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_date', 'location']

class HackathonForm(forms.ModelForm):
    class Meta:
        model = Hackathon
        fields = ['title', 'description', 'submission_deadline']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'contact_info']

class LearningResourceForm(forms.ModelForm):
    class Meta:
        model = LearningResource
        fields = ['title', 'link', 'description', 'tags']

class ProgressTrackingForm(forms.ModelForm):
    class Meta:
        model = ProgressTracking
        fields = ['goal', 'deadline', 'progress']
