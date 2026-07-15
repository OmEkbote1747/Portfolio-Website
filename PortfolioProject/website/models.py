from django.db import models

# Create your models here.

class Skill(models.Model):

    CATEGORY_CHOICES = [
        ("Programming", "Programming"),
        ("Frontend", "Frontend"),
        ("Backend", "Backend"),
        ("Database", "Database"),
        ("Tools", "Tools"),
        ("Cloud", "Cloud"),
    ]

    name = models.CharField(max_length=50)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    proficiency = models.PositiveSmallIntegerField(
        help_text="Enter a value between 0 and 100."
    )

    icon = models.ImageField(
        upload_to="skills/",
        blank=True,
        null=True
    )

    display_order = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name


class Project(models.Model):

    STATUS_CHOICES = [
        ("Completed", "Completed"),
        ("In Progress", "In Progress"),
    ]

    title = models.CharField(
        max_length=150
    )

    slug = models.SlugField(
        unique=True
    )

    short_description = models.CharField(
        max_length=250
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    github_url = models.URLField(
        blank=True
    )

    live_demo = models.URLField(
        blank=True
    )

    # Want to Add Dynamic technologies instead of simple String
    technologies = models.CharField(
        max_length=250
    )

    featured = models.BooleanField(
        default=False
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Completed"
    )

    created_at = models.DateField()

    class Meta:

        ordering = [
            "-created_at"
        ]

    def __str__(self):

        return self.title




class Certificate(models.Model):

    title = models.CharField(
        max_length=200
    )

    organization = models.CharField(
        max_length=150
    )

    issue_date = models.DateField()

    certificate_image = models.ImageField(
        upload_to="certificates/",
        blank=True,
        null=True
    )

    credential_url = models.URLField(
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        ordering = [
            "display_order",
            "-issue_date"
        ]

    def __str__(self):
        return self.title

class ContactMessage(models.Model):

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    sent_at = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    class Meta:

        ordering = [
            "-sent_at"
        ]

    def __str__(self):

        return f"{self.name} - {self.subject}"


class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)

    short_bio = models.TextField()

    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    resume = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    location = models.CharField(
        max_length=100,
        blank=True
    )

    github = models.URLField(
        blank=True
    )

    linkedin = models.URLField(
        blank=True
    )

    instagram = models.URLField(
        blank=True
    )

    about = models.TextField(
        blank=True,
        help_text="Detailed About Me section."
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.full_name

class Journey(models.Model):

    title = models.CharField(
        max_length=150
    )

    description = models.TextField()

    organization = models.CharField(
        max_length=150,
        blank=True
    )

    date = models.DateField()

    display_order = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        ordering = [
            "date",
            "display_order"
        ]

    def __str__(self):
        return self.title