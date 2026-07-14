from django.db import models

# Create your models here.

class Skill(models.Model):

    CATEGORY_CHOICES = [
        #Why Tuple?
        ("Programming", "Programming"),
        ("Frontend", "Frontend"),
        ("Backend", "Backend"),
        ("Database", "Database"),
        ("Tools", "Tools"),
        ("Cloud", "Cloud"),
    ]

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    percentage = models.PositiveIntegerField(default=80)
    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Iconify or Font Awesome class"
    )

    class Meta:
        ordering = ["category", "name"]

    def __str__(self):
        return self.name

class Project(models.Model):

    STATUS = [
        ("Completed", "Completed"),
        ("In Progress", "In Progress"),
    ]

    title = models.CharField(max_length=150)

    slug = models.SlugField(unique=True)

    short_description = models.CharField(max_length=250)

    description = models.TextField()

    image = models.ImageField(upload_to="projects/")

    github = models.URLField(blank=True)

    live_demo = models.URLField(blank=True)

    technologies = models.CharField(
        max_length=300,
        help_text="Python, Django, Tailwind"
    )

    featured = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Completed"
    )

    created = models.DateField()

    def __str__(self):
        return self.title

class Education(models.Model):

    institute = models.CharField(max_length=200)

    degree = models.CharField(max_length=150)

    duration = models.CharField(max_length=50)

    cgpa = models.CharField(max_length=20, blank=True)

    description = models.TextField(blank=True)

    def __str__(self):
        return self.degree

class Experience(models.Model):

    company = models.CharField(max_length=150)

    position = models.CharField(max_length=150)

    duration = models.CharField(max_length=50)

    description = models.TextField()

    technologies = models.CharField(max_length=250)

    def __str__(self):
        return self.company

class Certificate(models.Model):

    title = models.CharField(max_length=200)

    organization = models.CharField(max_length=150)

    issue_date = models.DateField()

    credential_url = models.URLField(blank=True)

    image = models.ImageField(upload_to="certificates/")

    def __str__(self):
        return self.title

class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=150)

    message = models.TextField()

    sent_at = models.DateTimeField(auto_now_add=True)

    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name