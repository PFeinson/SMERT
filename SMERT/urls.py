from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProfessionalManager.urls')),
    path('', include('CompanyManager.urls')),
    path('', include('RecruiterManager.urls')),
    path('', include('SkillsManager.urls')),
    path('', include('RoleManager.urls')),
]
