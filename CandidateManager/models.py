from django.db import models
from ..ProfessionalManager import Professional
from ..RoleManager import Role
from ..CompanyManager import Company
from ..OpenRoleManager import OpenRole
from ..PreviousRoleManager import PreviousRole
from ..CompanyManager import HiringCompany
from ..SkillsManager import Skill

class candidate (Professional):
    def create_candidate (request_data, self):
        # Create model response dictionary
        model_response = {}
        error_list = []
        model_response['status'] = True
        # Validate candidate Name
        if request_data['candidate_name']:
            if request_data['candidate_name'].length < 1:
                model_response['status'] = False
                error_list.append("Name must be at least one character long")
            else:
                model_response['status'] = False
                error_list.append("Name not provided")
        # Validate candidate Birth Date
        if request_data['candidate_birth_date']:
            # This validation is going to require some timedate delta shit I'll write later
            if request_data['candidate_birth_date'] < 18:
                # Using 18 as a semi-arbitrary age, need to check with legal/HR
                model_response['status'] = False
                error_list.append("candidate must be at least 18 years old")
        else:
            model_response['status'] = False
            error_list.append("Birth Date not provided")
        # Validate candidate Contact Information
        if request_data['candidate_address']:
            # Need to hook in an address verification method
            if not request_data['candidate_address'].verification:
                model_response['status'] = False
                error_list.append("Address cannot be verified")
        else:
            model_response['status'] = False
            error_list.append("Address not provided")
        if request_data['candidate_phone_number']:
            # Need to hook in a phone number verification method
            if not request_data['candidate_phone_number'].verification:
                model_response['status'] = False
                error_list.append("Phone number is not verified")
        else:
            model_response['status'] = False
            error_list.append("Phone number not provided")
        if request_data['candidate_email_address']:
            # Need to hook in an email verification method
            if not request_data['candidate_email_address'].verification:
                model_response['status'] = False
                error_list.append("Email is not verified")
        else:
            model_response['status'] = False
            error_list.append("Email not provided")
        
        # Create new Candidate
        if model_response['status']:
            new_candidate = Professional(
                candidate_name = request_data['candidate_name'],
                candidate_birth_date = request_data['candidate_birth_date'],
                candidate_address = request_data['candidate_address'],
                candidate_phone_number = request_data['candidate_phone_number'],
                candidate_email = request_data['candidate_email']
            )
            new_candidate.save()
            model_response['new_candidate'] = new_candidate
            model_response['status'] = True

class candidate (Professional):
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
    ) # Dictionary<Skill, candidate>
    unvetted_skills = models.list.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
    )
    # Company Information
    currentHiringCompanyPlacedAt = models.ForeignKey(
        HiringCompany,
        on_delete=models.CASCADE,
    )
    