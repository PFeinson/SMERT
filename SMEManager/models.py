from django.db import models
from ..ProfessionalManager import Professional
from ..SkillsManager import Skill
from ..CandidateManager import Candidate
from ..CompanyManager import HiringCompany

class SME (Professional):
    # Relational Data

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