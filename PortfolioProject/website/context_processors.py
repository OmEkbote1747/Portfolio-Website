from .models import (
    Profile,
    Skill,
    Project,
    Certificate,
)


def profile_context(request):

    profile = Profile.objects.filter(
        is_active=True
    ).first()

    return {

        "profile": profile,

        "project_count": Project.objects.count(),

        "skill_count": Skill.objects.count(),

        "certificate_count": Certificate.objects.count(),

    }