from django.db import models
from ..ProfessionalManager import Professional
from ..RoleManager import Role
from ..CompanyManager import Company
from ..OpenRoleManager import OpenRole
from ..PreviousRoleManager import PreviousRole
from ..CompanyManager import HiringCompany
from ..SkillsManager import Skill

class Candidate (Professional):
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
        Skill,
        on_delete = models.CASCADE
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
    