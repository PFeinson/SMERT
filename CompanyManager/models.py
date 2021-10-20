from django.db import models
from ..ProfessionalManager.models import SME, Candidate
from ..RoleManager import Role
from ..OpenRoleManager import OpenRole
from ..PreviousRoleManager import PreviousRole

class HiringCompanyManager(models.Manager):
    def create_new_hiring_company(request_data, self):
        # Create model response dictionary
        model_response = {}
        error_list = []
        model_response['status'] = True
        # Validations
        # Validate Company Name
        if request_data['company_name']:
            if len(request_data['company_name']) < 1 :
                model_response['status'] = False
                error_list.append("Company name not long enough")
            if len(request_data['company_name']) > 255 :
                model_response['status'] = False
                error_list.append("Company name cannot exceed 255 characters")
        else:
            model_response['status'] = False
            error_list.append("No company name provided.")
        # Company logo not required
        # Validate Company Address
        if request_data['company_address']:
            # will likely want some regex for validation here
            if len(request_data['company_address']) < 1 :  
                model_response['status'] = False
                error_list.append("Company address not long enough")
            if len(request_data['company_address']) > 255 :
                model_response['status'] = False
                error_list.append("Company address cannot exceed 255 characters")
        else:
            model_response['status'] = False
            error_list.append("No company address provided.")
        # Validate Company Phone Number
        if request_data['company_contact_phone_number']:
            # will likely want some regex for validation here
            if len(request_data['company_contact_phone_number']) < 10 :  
                model_response['status'] = False
                error_list.append("Company phone number not long enough")
            # if len(request_data['company_contact_phone_number']) > 10 :
            #     model_response['status'] = False
            #     error_list.append("Company phone number cannot exceed 255 characters")
        else:
            model_response['status'] = False
            error_list.append("No company phone number provided.")
        # Validate Company Bio
        if request_data['company_bio']:
            # will likely want some regex for validation here
            if len(request_data['company_bio']) < 1 :  
                model_response['status'] = False
                error_list.append("Company bio not long enough")
            if len(request_data['company_bio']) > 255 :
                model_response['status'] = False
                error_list.append("Company bio cannot exceed 255 characters")
        else:
            model_response['status'] = False
            error_list.append("No company bio provided.")
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
        SME.name,
        on_delete=models.CASCADE,
    )
    # SMEs who successfully have filled roles at this company
    previous_contracted_SMEs = models.list.ForeignKey(
        SME.name,
        on_delete=models.CASCADE,
    )
    # Candidates who haven't matriculated yet
    probationary_placements = models.ForeignKey(
        Candidate.name,
        on_delete = models.CASCADE,
    )
    # Historical record of all Candidates placed at Roles at this Company
    placed_applicants = models.list.ForeignKey(
        Candidate.name,
        on_delete = models.CASCADE,
    )
    # Historical record of all Candidates who have fai
    # led to matriculate
    failed_applicants = models.list.ForeignKey(
        Candidate.name,
        on_delete = models.CASCADE,
    )
    # Role Information
    # Roles currently open
    open_roles = models.List.ForeignKey(
        OpenRole.role_name,
        on_delete = models.CASCADE
    )
    # Roles previously filled
    previous_roles = models.List.ForeignKey(
        PreviousRole.role_name,
        on_delete = models.CASCADE
    )
    # Are they hiring
    currently_hiring = models.BooleanField()
    # Are they a first time customer
    successfully_contracted_with = models.BooleanField()
