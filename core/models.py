from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()

    profile_image = models.ImageField(upload_to='profile/', blank=True)

    email = models.EmailField()
    phone = models.CharField(max_length=20)

    location = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)

    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.name



class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Percentage (0-100)")

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    gpa = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.degree



class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField()

    achievements = models.TextField(
        blank=True,
        help_text="Separate achievements using | symbol"
    )

    def get_achievements_list(self):
        if self.achievements:
            return self.achievements.split('|')
        return []

    def __str__(self):
        return f"{self.role} at {self.company}"

