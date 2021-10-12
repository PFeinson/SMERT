from django.db import models

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=255),
    role_description = models.CharField(max_length=255),
    compensation_amount = models.FloatField(),
    total_compensation_amount = models.FloatField(),
    required_skills = models.list # List<Skills>

class OpenRole(Role):
    qualified_candidates = models.list # qualified candidates
    interviewed_candidates = models.list # candidates interviewed for this role
    declined_candidates = models.list # candidates declined for this role
    companies_currently_seeking_this_role = models.list # Companies who have this role open
    eligable_interviewing_smes = models.list # SMEs qualified to interview for this role
    
class PreviousRole(Role):
    candidates_who_have_held_this_role = models.list # candidates with this xp
    companies_filled_this_role_with_us = models.list # companies who hae filled this role wth us
    smes_with_experience_with_this_role = models.list # SMEs
