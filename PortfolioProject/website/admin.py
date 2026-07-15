from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "status",
        "featured",
        "created_at",
    )

    prepopulated_fields = {
        "slug": (
            "title",
        )
    }

    search_fields = (
        "title",
    )

    list_filter = (
        "status",
        "featured",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "proficiency",
        "display_order",
    )

    list_filter = (
        "category",
    )

    ordering = (
        "display_order",
    )

    search_fields = (
        "name",
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "title",
        "email",
        "location",
        "is_active",
    )

    search_fields = (
        "full_name",
        "title",
    )

    list_filter = (
        "is_active",
    )

@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "organization",
        "date",
        "display_order",
    )

    ordering = (
        "date",
    )

    search_fields = (
        "title",
        "organization",
    )

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "organization",
        "issue_date",
        "display_order",
    )

    search_fields = (
        "title",
        "organization",
    )

    ordering = (
        "display_order",
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "sent_at",
        "is_read",
    )

    list_filter = (
        "is_read",
    )

    search_fields = (
        "name",
        "email",
        "subject",
    )

    ordering = (
        "-sent_at",
    )