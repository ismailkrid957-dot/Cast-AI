from django.contrib import admin
from .models import Scenario, Role


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ("titre", "cree_par", "date_creation")
    list_filter = ("date_creation",)
    search_fields = ("titre", "description")


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("titre", "scenario", "date_creation")
    search_fields = ("titre", "scenario__titre")
    list_filter = ("date_creation",)
