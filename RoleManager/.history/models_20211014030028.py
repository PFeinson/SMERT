from django.db import models

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
        if (model_response['status']:
            # Create new Role
            new_role = Role(
                role_name = request_data['role_name'], 
                role_description = request_data['role_description'],
                compensation_amount = request_data['compensation_amount'],
                total_compensation_amount = request_data['total_compensation_amount'],
                required_skills = request_data['required_skills']
            )
class Role(models.Model):
    role_name = models.CharField(max_length=255),
    role_description = models.CharField(max_length=255),
    compensation_amount = models.FloatField(),
    total_compensation_amount = models.FloatField(),
    required_skills = models.list # List<Skills>

class OpenRole(Role):
    qualified_candidates = models.list # qualified candidates
    interviewed_candidates = models.list # candidates interviewed for this role
    declined_candidates = models.list # candidates declined for this role
    companies_currently_seeking_this_role = models.list # Companies who have this role open
    eligable_interviewing_smes = models.list # SMEs qualified to interview for this role
    
class PreviousRole(Role):
    candidates_who_have_held_this_role = models.list # candidates with this xp
    companies_filled_this_role_with_us = models.list # companies who hae filled this role wth us
    smes_with_experience_with_this_role = models.list # SMEs
