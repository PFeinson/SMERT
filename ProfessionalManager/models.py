from django.db import models
from ..CompanyManager.models import HiringCompany

class Professional(models.Model):
    # Relational Data
    roles_held = models.__dict__ # Dictionary<Role, Company>
    skills_claimed = models.list # List<Skill>
    # Professional Demographics Information
    name = models.CharField(max_length=255)
    profile_picture = models.FileField(upload_to="media/")
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10) # Does not cover international
    email_address = models.CharField(max_length=255) 

    

class Candidate (models.Model):
    # Relational Data
    held_roles = models.__dict__ # Dictionary<HiringCompany, PreviousRole>
    potential_roles = models.list # List<OpenRole>
    # Skills Information
    vetted_skills = models.__dict__ # Dictionary<Skill, SME>
    unvetted_skills = models.list # List<Skill>
    # Company Information
    currentHiringCompanyPlacedAt = models.ForeignKey(
        HiringCompany,
        on_delete=models.CASCADE,
    )
    previousHiringCompaniesPlacedAt = models.list.ForeignKey(
        HiringCompany,
        on_delete=models.CASCADE,
    )
