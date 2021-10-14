from django.db import models

class RoleManager(models.manager):
    def create_role (request_data, self):
        # Create model response dictionary
        model_response = {}
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
