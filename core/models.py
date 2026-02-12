from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    # Personal Information
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    # Contact Information
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    
    # Social Links
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    medium = models.URLField(blank=True)
    
    # Professional Summary
    professional_summary = models.TextField(
        blank=True,
        help_text="Detailed professional summary for resume sidebar"
    )
    
    # Availability
    AVAILABILITY_CHOICES = [
        ('available', 'Available for Work'),
        ('open', 'Open to Opportunities'),
        ('busy', 'Not Available'),
    ]
    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default='available'
    )
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Skill Categories"
        ordering = ['order']

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name='skills',
        blank=True,
        null=True
    )
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Percentage (0-100)"
    )
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', '-proficiency']

    def __str__(self):
        return f"{self.name} - {self.proficiency}%"


class Language(models.Model):
    PROFICIENCY_LEVELS = [
        ('native', 'Native'),
        ('professional', 'Professional Working'),
        ('conversational', 'Conversational'),
        ('basic', 'Basic'),
    ]
    
    name = models.CharField(max_length=50)
    proficiency = models.CharField(
        max_length=20,
        choices=PROFICIENCY_LEVELS,
        default='professional'
    )
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.get_proficiency_display()}"


class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-year', 'order']

    def __str__(self):
        return f"{self.name} - {self.issuer}"


class Interest(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=50,
        help_text="Font Awesome icon class (e.g., 'fa-camera')",
        default='fa-circle'
    )
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_year = models.CharField(max_length=20, blank=True)
    end_year = models.CharField(max_length=20)
    gpa = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    achievements = models.TextField(
        blank=True,
        help_text="Separate achievements with | symbol"
    )
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-end_year', 'order']

    def get_achievements_list(self):
        if self.achievements:
            return [a.strip() for a in self.achievements.split('|') if a.strip()]
        return []

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Experience(models.Model):
    EMPLOYMENT_TYPE = [
        ('fulltime', 'Full-time'),
        ('parttime', 'Part-time'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
    ]
    
    company = models.CharField(max_length=200)
    company_website = models.URLField(blank=True)
    role = models.CharField(max_length=200)
    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPE,
        default='fulltime'
    )
    location = models.CharField(max_length=200, blank=True)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20, blank=True, help_text="Leave blank for current")
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    achievements = models.TextField(
        blank=True,
        help_text="Separate achievements with | symbol"
    )
    technologies = models.CharField(
        max_length=500,
        blank=True,
        help_text="Separate technologies with | symbol"
    )
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date', 'order']

    def get_achievements_list(self):
        if self.achievements:
            return [a.strip() for a in self.achievements.split('|') if a.strip()]
        return []
    
    def get_technologies_list(self):
        if self.technologies:
            return [t.strip() for t in self.technologies.split('|') if t.strip()]
        return []

    def __str__(self):
        return f"{self.role} at {self.company}"


class Project(models.Model):
    PROJECT_STATUS = [
        ('completed', 'Completed'),
        ('ongoing', 'Ongoing'),
        ('archived', 'Archived'),
    ]
    
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    technologies = models.CharField(
        max_length=500,
        help_text="Separate technologies with | symbol"
    )
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=PROJECT_STATUS,
        default='completed'
    )
    featured = models.BooleanField(default=False)
    start_date = models.CharField(max_length=20, blank=True)
    end_date = models.CharField(max_length=20, blank=True)
    highlights = models.TextField(
        blank=True,
        help_text="Separate highlights with | symbol"
    )
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-featured', 'order', '-start_date']

    def get_technologies_list(self):
        if self.technologies:
            return [t.strip() for t in self.technologies.split('|') if t.strip()]
        return []
    
    def get_highlights_list(self):
        if self.highlights:
            return [h.strip() for h in self.highlights.split('|') if h.strip()]
        return []

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-year', 'order']

    def __str__(self):
        return f"{self.title} - {self.issuer}"


class Publication(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-date', 'order']

    def __str__(self):
        return self.title