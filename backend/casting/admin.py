
from django.contrib import admin
from .models import Scenario


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('titre', 'cree_par', 'date_creation')
    list_filter = ('date_creation',)
    search_fields = ('titre', 'description')
