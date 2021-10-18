from django.db import models
from ..ProfessionalManager.models import SME, Candidate
from ..RoleManager import Role
from ..OpenRoleManager import OpenRole
from ..PreviousRoleManager import PreviousRole

class HiringCompanyManager(models.Manager):
    def create_new_hiring_company(self):
        model_response = {}
    # Validations
    # (>=1 && <= 255 = Length)
    # company_name >= 1 && <= 255
    # company_logo not required
    # company_address >= 1 && <= 255
    # company_contact_phone_number >= 1 && <= 10
    # company_bio >= 1 && <= 10
        return model_response

class Company(models.Model):
    # Company Information
    company_name = models.CharField(max_length=255)
    company_logo = models.FileField(upload_to="media/")
    company_address = models.CharField(max_length=255)
    company_contact_phone_number = models.CharField(max_length=255)
    company_contact_email_address = models.CharField(max_length=255)
    company_bio = models.CharField(max_length=255)
    company_rating = models.FloatField()


class HiringCompany(Company):
    # Relational Data
    # SMEs currently filling Roles at this compamy 
    currently_contracted_SMEs = models.list.ForeignKey(
        SME,
        on_delete=models.CASCADE,
    )
    # SMEs who successfully have filled roles at this company
    previous_contracted_SMEs = models.list.ForeignKey(
        SME,
        on_delete=models.CASCADE,
    )
    # Candidates who haven't matriculated yet
    probationary_placements = models.ForeignKey(
        Candidate,
        on_delete = models.CASCADE,
    )
    # Historical record of all Candidates placed at Roles at this Company
    placed_applicants = models.list.ForeignKey(
        Candidate,
        on_delete = models.CASCADE,
    )
    # Historical record of all Candidates who have fai
    # led to matriculate
    failed_applicants = models.list.ForeignKey(
        Candidate,
        on_delete = models.CASCADE,
    )
    # Role Information
    # Roles currently open
    open_roles = models.List.ForeignKey(
        OpenRole,
        on_delete = models.CASCADE
    )
    # Roles previously filled
    previous_roles = models.List.ForeignKey(
        PreviousRole,
        on_delete = models.CASCADE
    )
    # Are they hiring
    currently_hiring = models.BooleanField()
    # Are they a first time customer
    successfully_contracted_with = models.BooleanField()
