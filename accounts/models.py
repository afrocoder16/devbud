from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Additional profile details
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)
    
    EXPERIENCE_CHOICES = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, blank=True)
    interests = models.TextField(blank=True, help_text="Comma-separated list of interests (e.g., Django, React)")
    
    # Existing fields
    bio = models.TextField(blank=True)
    skills = models.CharField(
        max_length=255, 
        blank=True, 
        help_text="Comma-separated list of skills (e.g., Python, JavaScript)"
    )
    mentor = models.BooleanField(default=False, help_text="Indicates if user is available for mentorship")

    def __str__(self):
        return self.user.username
