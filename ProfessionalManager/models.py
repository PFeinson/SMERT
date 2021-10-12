from django.db import models
from ..CompanyManager.models import HiringCompany
from ..RoleManager.models import *
from ..SkillsManager.models import *

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
    potential_roles = models.list.ForeignKey(
        OpenRole,
        on_delete=models.CASCADE,
    )
    # Skills Information
    vetted_skills = models.__dict__ # Dictionary<Skill, SME>
    unvetted_skills = models.list.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
    )
    # Company Information
    currentHiringCompanyPlacedAt = models.ForeignKey(
        HiringCompany,
        on_delete=models.CASCADE,
    )
    previousHiringCompaniesPlacedAt = models.list.ForeignKey(
        HiringCompany,
        on_delete=models.CASCADE,
    )

class SME (models.Model):
    # Relational Data

    # Skills Vetted By
    skills_vetted_by = models.__dict__ # Dictionary<SME, Skill>
    # SME Candidate Information
    vetted_candidate_skills = models.__dict__ # Dictionary<Candidate, Skill>
    candidates_placed = models.list.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
    )
    failed_candidate_placement = models.list.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
    )
    successful_candidate_placement = models.list.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
    )
    # SME Company information
    companies_worked_with = models.list.ForeignKey(
        HiringCompany,
        on_delete=models.CASCADE,
    )
    companies_with_successful_placements = models.list.ForeignKey(
        HiringCompany,
        on_delete=models.CASCADE,
    )
    companies_with_failed_placements = models.list.ForeignKey(
        HiringCompany,
        on_delete=models.CASCADE,
    )
   
   