from django.db import models
from ..ProfessionalManager import Professional
from ..SkillsManager import Skill
from ..CandidateManager import Candidate
from ..CompanyManager import HiringCompany

class SME (Professional):
    def create_SME (request_data, self):
        # Create model response dictionary
        model_response = {}
        error_list = []
        model_response['status'] = True
        # Validate SME Name
        if request_data['SME_name']:
            if request_data['SME_name'].length < 1:
                model_response['status'] = False
                error_list.append("Name must be at least one character long")
            else:
                model_response['status'] = False
                error_list.append("Name not provided")
        # Validate SME Birth Date
        if request_data['SME_birth_date']:
            # This validation is going to require some timedate delta shit I'll write later
            if request_data['SME_birth_date'] < 18:
                # Using 18 as a semi-arbitrary age, need to check with legal/HR
                model_response['status'] = False
                error_list.append("SME must be at least 18 years old")
        else:
            model_response['status'] = False
            error_list.append("Birth Date not provided")
        # Validate SME Contact Information
        if request_data['SME_address']:
            # Need to hook in an address verification method
            if not request_data['SME_address'].verification:
                model_response['status'] = False
                error_list.append("Address cannot be verified")
        else:
            model_response['status'] = False
            error_list.append("Address not provided")
        if request_data['SME_phone_number']:
            # Need to hook in a phone number verification method
            if not request_data['SME_phone_number'].verification:
                model_response['status'] = False
                error_list.append("Phone number is not verified")
        else:
            model_response['status'] = False
            error_list.append("Phone number not provided")
        if request_data['SME_email_address']:
            # Need to hook in an email verification method
            if not request_data['SME_email_address'].verification:
                model_response['status'] = False
                error_list.append("Email is not verified")
        else:
            model_response['status'] = False
            error_list.append("Email not provided")
        
        # Create new SME
        if model_response['status']:
            new_SME = Professional(
                SME_name = request_data['SME_name'],
                SME_birth_date = request_data['SME_birth_date'],
                SME_address = request_data['SME_address'],
                SME_phone_number = request_data['SME_phone_number'],
                SME_email = request_data['SME_email']
            )
            new_SME.save()
            model_response['new_SME'] = new_SME
            model_response['status'] = True



    # Relational Data

class SME(Professional):
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