from django.db import models
from ..ProfessionalManager.models import *  
class Role(models.Model):
    role_name = models.CharField(max_length=255),
    role_description = models.CharField(max_length=255),
    compensation_amount = models.FloatField(),
    total_compensation_amount = models.FloatField(),
    # Skills required for this job
    required_skills = models.list.ForeignKey(
        Skill.skill_name,
        on_delete = models.CASCADE,
    ) 


    
