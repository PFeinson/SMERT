from django.db import models
from ..RoleManager import Role
from ..ProfessionalManager import Candidate, SME
from ..CompanyManager import HiringCompany

class PreviousRoleManager(models.Manager):
    def __str__():
        return "previous role"

class PreviousRole(Role):
    # candidates with this xp
    candidates_who_have_held_this_role = models.list.ForeignKey(
        Candidate.name,
        on_delete = models.CASCADE,
    ) 
    # companies who hae filled this role wth us
    companies_filled_this_role_with_us = models.list.ForeignKey(
        HiringCompany.company_name,
        on_delete = models.CASCADE,
    ) 
    # SMEs who can vet for this role
    smes_with_experience_with_this_role = models.list.ForeignKey(
        SME.name,
        on_delete = models.CASCADE,
    ) 
    previous_roles = PreviousRoleManager()
