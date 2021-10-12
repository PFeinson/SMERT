from django.db import models

# Create your models here.

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
    currently_contracted_SMEs = models.list # List<SME>
    previous_contracted_SMEs = models.list # List<SME>
    probationary_placements = models.__dict__ # Dictionary<Candidate, Role>
    placed_applicants = models.__dict__ # Dictionary<Candidate, PreviousRole>
    failed_applicants = models.__dict__ # Dictionary<Candidate, Role>
    # Role Information
    open_roles = models.List # List<OpenRole>
    previous_roles = models.List #List<PreviousRole>
    currently_hiring = models.BooleanField()
    successfully_contracted_with = models.BooleanField()