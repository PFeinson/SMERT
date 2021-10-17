from typing import Match
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import Field
from ..CompanyManager.models import HiringCompany
from ..SkillsManager.models import Skill
from ..RoleManager.models import Role
from ..PreviousRoleManager import PreviousRole
from ..OpenRoleManager import OpenRole
from . import *
class Professional(models.Model):
    # Relational Data
    roles_held = models.list.ForeignKey(
        Role,
        on_delete = CASCADE,
    )
    skills_claimed = models.list.ForeignKey(
        Skill,
        on_delete = CASCADE
    )
    # Professional Demographics Information
    name = models.CharField(max_length=255)
    profile_picture = models.FileField(upload_to="media/")
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10) # Does not cover international
    email_address = models.CharField(max_length=255) 

    def __str__(self):
        return "Name: " + self.name + "\n"