"""
URL configuration for AI Travel Assistant project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='dashboard:home', permanent=False)),
    path('accounts/', include('accounts.urls')),
    path('translate/', include('translations.urls')),
    path('phrasebook/', include('phrasebook.urls')),
    path('dashboard/', include('dashboard.urls')),
]
