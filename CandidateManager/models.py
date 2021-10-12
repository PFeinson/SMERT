from django.db import models

# Create your models here.
class Candidate (models.Model):
    # Relational Data
    held_roles = models.__dict__ # Dictionary<HiringCompany, PreviousRole>
    potential_roles = models.list # List<OpenRole>
    # Skills Information
    vetted_skills = models.__dict__ # Dictionary<Skill, SME>
    unverfied_skills = models.list # List<Skill>
    # Company Information
    