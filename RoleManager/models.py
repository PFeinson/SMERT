from django.db import models
from ..ProfessionalManager.models import *
class RoleManager(models.manager):
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
                error_list.append('role name can not exceed 255 characters')
        else:
            model_response['status'] = False
            error_list.append("role name not provided.")   
        # Validate Role Description                    
        if request_data['role_description']:
            if len(request_data['role_description']) < 1 :
                model_response['status'] = False
                error_list.append("Role description must be at least 1 character lonng")
            if len(request_data['role_description']) > 255 :
                model_response['status'] = False
                error_list.append("Role deescription can not exceeed 255 characters")         
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
        # Validate required_skills    
        if model_response['status']:
            # Create new Role
            new_role = Role(
                role_name = request_data['role_name'], 
                role_description = request_data['role_description'],
                compensation_amount = request_data['compensation_amount'],
                total_compensation_amount = request_data['total_compensation_amount'],
                required_skills = request_data['required_skills']
            )
            new_role.save()
            model_response['new_role'] = new_role
            model_response['status'] = True
            
class Role(models.Model):
    role_name = models.CharField(max_length=255),
    role_description = models.CharField(max_length=255),
    compensation_amount = models.FloatField(),
    total_compensation_amount = models.FloatField(),
    # Skills required by this job
    required_skills = models.list.ForeignKey(
        Skill,
        on_delete = models.CASCADE,
    ) 

class OpenRole(Role):
    qualified_candidates = models.list.ForeignKey(
        Candidate,
        on_delete = models.CASCADE, 
    )# qualified candidate
    interviewed_candidates = models.list.ForeignKey(
        Candidate,
        on_delete = models.CASCADE,
    )# candidates interviewed for this role
    declined_candidates = models.list.ForeignKey(
        Candidate,
        on_delete = models.CASCADE,
    ) # candidates declined for this role
    companies_currently_seeking_this_role = models.list.ForeignKey(
        HiringCompany,
        on_delete = models.CASCADE,
    ) # Companies who have this role open
    eligable_interviewing_smes = models.list.ForeignKey(
        SME,
        on_delete = models.CASCADE,
    ) # SMEs qualified to interview for this role
    
class PreviousRole(Role):
    # candidates with this xp
    candidates_who_have_held_this_role = models.list.ForeignKey(
        Candidate,
        on_delete = models.CASCADE,
    ) 
    # companies who hae filled this role wth us
    companies_filled_this_role_with_us = models.list.ForeignKey(
        HiringCompany,
        on_delete = models.CASCADE,
    ) 
    # SMEs who can vet for this role
    smes_with_experience_with_this_role = models.list.ForeignKey(
        SME,
        on_delete = models.CASCADE,
    ) 
