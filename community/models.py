from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    """
    Developer groups for collaboration and discussion.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(
        User,
        related_name='joined_groups',
        blank=True,
        help_text='Users who have joined this group'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    """
    Community events such as meetups and workshops.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='events',
        help_text='User who created this event'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Hackathon(models.Model):
    """
    Coding competitions with submission deadlines.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    submission_deadline = models.DateTimeField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='hackathons',
        help_text='User who organized this hackathon'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Job(models.Model):
    """
    Job postings for developers.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    contact_info = models.CharField(max_length=200)
    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='jobs',
        help_text='User who posted this job'
    )
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class LearningResource(models.Model):
    """
    Curated tutorials, courses, and articles.
    """
    title = models.CharField(max_length=200)
    link = models.URLField()
    description = models.TextField(blank=True)
    tags = models.CharField(
        max_length=255,
        blank=True,
        help_text='Comma-separated tags for categorization'
    )
    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='resources',
        help_text='User who shared this resource'
    )
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class ProgressTracking(models.Model):
    """
    User progress towards learning or project goals.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='progresses',
        help_text='User whose progress is being tracked'
    )
    goal = models.CharField(max_length=200)
    deadline = models.DateTimeField()
    progress = models.PositiveIntegerField(
        default=0,
        help_text='Progress percentage (0-100)'
    )

    def __str__(self) -> str:
        return f"{self.user.username} - {self.goal} ({self.progress}%)"


class CommunityPost(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='community_posts',
        help_text='User who authored this post'
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_posts', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(CommunityPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
