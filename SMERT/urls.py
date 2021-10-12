from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CandidateManager.urls')),
    path('', include('CompanyManager.urls')),
    path('', include('SMEManager.urls')),
    path('', include('RecruiterManager.urls'))
]
