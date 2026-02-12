from django.contrib import admin
from .models import Profile, Skill, Education, Project, Experience


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'duration')
    search_fields = ('role', 'company')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies')
    search_fields = ('title',)


admin.site.register(Skill)

admin.site.site_header = "Portfolio Resume Admin"
admin.site.site_title = "Resume Admin"
admin.site.index_title = "Manage Your Resume Content"
