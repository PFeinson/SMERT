from typing import Match
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import Field
from ..CompanyManager.models import HiringCompany
from ..RoleManager.models import *
from ..SkillsManager.models import *
from ..ProfessionalManager import *
from . import *
class Professional(models.Model):
    # Relational Data
    roles_held = models.list.ForeignKey(
        Role,
        on_delete = CASCADE,
    )
    skills_claimed = models.list.ForeignKey(
        Skill,
        on_delete = CASCADE
    )
    # Professional Demographics Information
    name = models.CharField(max_length=255)
    profile_picture = models.FileField(upload_to="media/")
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10) # Does not cover international
    email_address = models.CharField(max_length=255) 
class Candidate (Professional):
    # Relational Data
    # Previous Employment Information
    previousHiringCompaniesPlacedAt = models.list.ForeignKey(
        HiringCompany.company_name,
        on_delete=models.CASCADE,
    )
    held_roles = models.list.ForeignKey(
        PreviousRole.role_name,
        on_delete = models.CASCADE
    )

    # Roles this candidate would be suited for
    potential_roles = models.list.ForeignKey(
        OpenRole.role_name,
        on_delete=models.CASCADE,
    )
    current_role = models.ForeignKey(
        Role.role_name,
        on_delete = models.CASCADE
    )
    # Skills Information
    vetted_skills = models.list.ForeignKey(
        SME,
        on_delete = CASCADE
    ) # Dictionary<Skill, SME>
    unvetted_skills = models.list.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
    )
    # Company Information
    currentHiringCompanyPlacedAt = models.ForeignKey(
        HiringCompany,
        on_delete=models.CASCADE,
    )
    

class SME (Professional):
    # Relational Data

    # Skills Vetted By
    skills_qualified_to_vet = models.list.ForeignKey(
        Skill.skill_name,
        on_delete = models.CASCADE,
    )
    # SME Candidate Information
    vetted_candidates = models.list.ForeignKey(
        Candidate.name,
        on_delete = models.CASCADE,
    )
    # Historical data of all Candidates placed
    candidates_placed = models.list.ForeignKey(
        Candidate.name,
        on_delete=models.CASCADE,
    )
    # Historical data of all Candidates who have failed to matriculate
    failed_candidate_placement = models.list.ForeignKey(
        Candidate.name,
        on_delete=models.CASCADE,
    )
    # Historical data of all Candidates who successfully matriculated
    successful_candidate_placement = models.list.ForeignKey(
        Candidate.name,
        on_delete=models.CASCADE,
    )
    # SME Company information
    companies_worked_with = models.list.ForeignKey(
        HiringCompany.company_name,
        on_delete=models.CASCADE,
    )
    companies_with_successful_placements = models.list.ForeignKey(
        HiringCompany.company_name,
        on_delete=models.CASCADE,
    )
    companies_with_failed_placements = models.list.ForeignKey(
        HiringCompany.company_name,
        on_delete=models.CASCADE,
    )

    def __str__():
        return ""