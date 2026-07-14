from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "status",
        "featured",
        "created"
    )

    search_fields = ("title",)

    list_filter = (
        "status",
        "featured"
    )

    prepopulated_fields = {
        "slug": ("title",)
    }


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "percentage"
    )


admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Certificate)
admin.site.register(Contact)