from django.db import models
from ..RoleManager import Role
from ..ProfessionalManager import Candidate, SME
from ..CompanyManager import HiringCompany

class PreviousRoleManager(models.Manager):
    def create_role (request_data, self):
        # Create model response dictionary
        model_response = {}
        error_list = []
        model_response['status'] = True
        # Validate Role Name
        if request_data['role_name']:
            if len(request_data['role_name']) < 1 : 
                model_response['status'] = False
                error_list.append("role name not long enough")
            if len(request_data['role_name']) > 255 :
                model_response['status'] = False
                error_list.append("role name can not exceed 255 characters")
        else:
            model_response['status'] = False
            error_list.append("role name not provided.")   
        # Validate Role Description                    
        if request_data['role_description']:
            if len(request_data['role_description']) < 1 :
                model_response['status'] = False
                error_list.append("Role description must be at least 1 character long")
            if len(request_data['role_description']) > 255 :
                model_response['status'] = False
                error_list.append("Role deescription cannot exceed 255 characters")         
        else:
            model_response['status'] = False
            error_list.append("No role description provided.")
        # Validate compensation amount
        if request_data['compensation_amount']:
            if request_data['compensation_amount'] < 0.01 :
                model_response['status'] = False
                error_list.append("Compensation cannot be less than 0.01")
        else:
            model_response['status'] = False
            error_list.append("Compensation amount not provided")        
        # Validate total_compensation_amount
        if request_data['total_compensation_amount']:
            if request_data['total_compensation_amount'] < request_data['compensation_amount'] :
                model_response['status'] = False
                error_list.append("Total compensation cannot be less than Base Compensation")
        else:
            model_response['status'] = False
            error_list.append("Total Compensation Amount not provided")  
        # Validate dates role was held
        # this requires datetime wizardry that I think I need to write some forms to test
                
            
        if model_response['status']:
            # Create new Role to base new previous role on
            new_role = Role(
                role_name = request_data['role_name'], 
                role_description = request_data['role_description'],
                compensation_amount = request_data['compensation_amount'],
                total_compensation_amount = request_data['total_compensation_amount'],
                held_dates = request_data['held_dates']
            )
            # Create new PreviousRole
            if model_response['is_new_role']:
                new_previous_role = PreviousRole(new_role)
            new_role.save()
            model_response['new_role'] = new_role
            model_response['status'] = True 

class PreviousRole(Role):
    # candidates with this xp
    candidates_who_have_held_this_role = models.list.ForeignKey(
        Candidate.name,
        on_delete = models.CASCADE,
    ) 
    # companies who have filled this role wth us
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
