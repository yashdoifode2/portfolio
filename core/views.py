from django.shortcuts import render
from .models import Profile, Skill, Education, Project, Experience

def home(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
        'skills': Skill.objects.all(),
        'education': Education.objects.all(),
        'projects': Project.objects.all(),
        'experience': Experience.objects.all(),
    }

    return render(request, 'home.html', context)
