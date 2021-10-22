from django.db import models
from ..RoleManager import Role
from ..ProfessionalManager import Candidate, SME
from ..CompanyManager import HiringCompany

class OpenRoleManager(models.manager):
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
        # Validate required_skills  
          
        if model_response['status']:
            # Create new Role to base new open role on
            new_role = Role(
                role_name = request_data['role_name'], 
                role_description = request_data['role_description'],
                compensation_amount = request_data['compensation_amount'],
                total_compensation_amount = request_data['total_compensation_amount'],
                required_skills = request_data['required_skills']
            )
            # Create new OpenRole
            if model_response['is_new_role']:
                new_open_role = OpenRole(new_role)
                new_open_role.qualified_candidates = Candidate.filter()
            new_role.save()
            model_response['new_role'] = new_role
            model_response['status'] = True
          

class OpenRole(Role):
    # qualified candidate
    qualified_candidates = models.list.ForeignKey(
        Candidate.name,
        on_delete = models.CASCADE, 
    )
    # candidates interviewed for this role
    interviewed_candidates = models.list.ForeignKey(
        Candidate.name,
        on_delete = models.CASCADE,
    )
    # candidates declined for this role
    declined_candidates = models.list.ForeignKey(
        Candidate.name,
        on_delete = models.CASCADE,
    ) 
    # Companies who have this role open
    companies_currently_seeking_this_role = models.list.ForeignKey(
        HiringCompany.company_name,
        on_delete = models.CASCADE,
    ) 
    # SMEs qualified to interview for this role
    eligable_interviewing_smes = models.list.ForeignKey(
        SME.name,
        on_delete = models.CASCADE,
    ) 
    open_roles = OpenRoleManager()