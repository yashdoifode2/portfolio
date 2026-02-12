from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Profile, SkillCategory, Skill, Language, Certification, 
    Interest, Education, Experience, Project, Achievement, Publication
)

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ['name', 'proficiency', 'is_featured', 'order']

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'skill_count']
    inlines = [SkillInline]
    
    def skill_count(self, obj):
        return obj.skills.count()
    skill_count.short_description = 'Number of Skills'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'is_featured', 'order']
    list_filter = ['category', 'is_featured']
    search_fields = ['name']
    list_editable = ['proficiency', 'is_featured', 'order']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'availability', 'display_image']
    list_editable = ['availability']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'bio', 'professional_summary', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location', 'website')
        }),
        ('Social Media', {
            'fields': ('linkedin', 'github', 'twitter', 'medium')
        }),
        ('Availability', {
            'fields': ('availability',)
        }),
    )
    
    def display_image(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 50%; object-fit: cover;" />',
                obj.profile_image.url
            )
        return "No Image"
    display_image.short_description = 'Profile Image'

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency', 'order']
    list_editable = ['proficiency', 'order']
    search_fields = ['name']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuer', 'year', 'order']
    list_filter = ['year', 'issuer']
    search_fields = ['name', 'issuer']
    list_editable = ['order']

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'order']
    list_editable = ['order']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'end_year', 'gpa', 'order']
    list_filter = ['institution', 'end_year']
    search_fields = ['degree', 'institution']
    list_editable = ['order']
    
    fieldsets = (
        ('Degree Information', {
            'fields': ('degree', 'field_of_study', 'institution', 'location')
        }),
        ('Dates', {
            'fields': ('start_year', 'end_year')
        }),
        ('Details', {
            'fields': ('gpa', 'description', 'achievements', 'order')
        }),
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'start_date', 'end_date', 'is_current', 'order']
    list_filter = ['company', 'employment_type', 'is_current']
    search_fields = ['role', 'company', 'description']
    list_editable = ['order', 'is_current']
    
    fieldsets = (
        ('Position Details', {
            'fields': ('role', 'employment_type', 'company', 'company_website', 'location')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Description', {
            'fields': ('description', 'achievements', 'technologies', 'order')
        }),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'featured', 'order', 'display_image']
    list_filter = ['status', 'featured']
    search_fields = ['title', 'description']
    list_editable = ['status', 'featured', 'order']
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'subtitle', 'description', 'status', 'featured')
        }),
        ('Media & Links', {
            'fields': ('image', 'github_link', 'live_link')
        }),
        ('Technologies & Highlights', {
            'fields': ('technologies', 'highlights')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'order')
        }),
    )
    
    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />',
                obj.image.url
            )
        return "No Image"
    display_image.short_description = 'Image'

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuer', 'year', 'order']
    list_filter = ['year', 'issuer']
    search_fields = ['title', 'issuer']
    list_editable = ['order']

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'date', 'order']
    list_filter = ['publisher', 'date']
    search_fields = ['title', 'publisher']
    list_editable = ['order']

# Customize Admin Site
admin.site.site_header = "Portfolio Resume Management System"
admin.site.site_title = "Resume CMS"
admin.site.index_title = "Welcome to Your Resume Dashboard"