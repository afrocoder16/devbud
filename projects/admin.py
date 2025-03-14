from django.contrib import admin
from .models import Project, ProjectImage, CollaborationRequest, Feedback

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('title', 'created_by', 'created_at')
    search_fields = ('title', 'tech_stack')

admin.site.register(Project, ProjectAdmin)
admin.site.register(CollaborationRequest)
admin.site.register(Feedback)
