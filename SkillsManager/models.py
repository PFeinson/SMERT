from django.db import models
from ..ProfessionalManager.models import *
from ..SMEManager.models import *
class Skill(models.Model):
    skill_name = models.CharField(max_length=255)
    # SME who vetted this particular skill for this particular candidate
    vetted_by = models.ForeignKey(
        SME,
        on_delete = models.CASCADE
    )
    # All Candidates who have this skill
    skill_held_by = models.list.ForeignKey(
        Candidate,
        on_delete = models.CASCADE,
    )