from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='joined_groups', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Hackathon(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    submission_deadline = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hackathons')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    contact_info = models.CharField(max_length=200)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class LearningResource(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    description = models.TextField(blank=True)
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags")
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resources')
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ProgressTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progresses')
    goal = models.CharField(max_length=200)
    deadline = models.DateTimeField()
    progress = models.PositiveIntegerField(default=0, help_text="Progress percentage")

    def __str__(self):
        return f"{self.user.username} - {self.goal}"
