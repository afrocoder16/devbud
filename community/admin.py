from django.contrib import admin
from .models import (
    Group,
    Event,
    Hackathon,
    Job,
    LearningResource,
    ProgressTracking,
    CommunityPost,     
)

admin.site.register(Group)
admin.site.register(Event)
admin.site.register(Hackathon)
admin.site.register(Job)
admin.site.register(LearningResource)
admin.site.register(ProgressTracking)
admin.site.register(CommunityPost)  
