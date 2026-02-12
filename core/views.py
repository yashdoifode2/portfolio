from django.shortcuts import render
from django.db.models import Prefetch
from .models import (
    Profile, SkillCategory, Skill, Language, Certification, 
    Interest, Education, Experience, Project, Achievement, Publication
)

def home(request):
    # Get profile (first one or create default context)
    profile = Profile.objects.first()
    
    # Build complete resume context
    context = {
        'profile': profile,
        
        # Skills organized by category
        'skill_categories': SkillCategory.objects.prefetch_related(
            Prefetch('skills', queryset=Skill.objects.all())
        ).all(),
        
        # Featured skills for sidebar
        'featured_skills': Skill.objects.filter(is_featured=True)[:8],
        
        # All skills with proficiency
        'skills': Skill.objects.all(),
        
        # Languages
        'languages': Language.objects.all(),
        
        # Certifications
        'certifications': Certification.objects.all(),
        
        # Interests
        'interests': Interest.objects.all(),
        
        # Education (ordered by year)
        'education': Education.objects.all(),
        
        # Experience (current first, then by date)
        'experience': Experience.objects.all(),
        
        # Featured projects
        'featured_projects': Project.objects.filter(featured=True)[:6],
        
        # All projects
        'projects': Project.objects.all(),
        
        # Achievements
        'achievements': Achievement.objects.all(),
        
        # Publications
        'publications': Publication.objects.all(),
    }
    
    return render(request, 'home.html', context)