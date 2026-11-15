
from django.contrib import admin
from .models import Audition, Evaluation


@admin.register(Audition)
class AuditionAdmin(admin.ModelAdmin):
    list_display = ('candidat', 'scenario', 'statut', 'date_soumission')
    list_filter = ('statut', 'date_soumission')
    search_fields = ('candidat__username', 'scenario__titre')


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('audition', 'score_global', 'date_evaluation')
    search_fields = ('audition__candidat__username',)
