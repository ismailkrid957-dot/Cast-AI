from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [("casting", "0001_initial")]
    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titre", models.CharField(max_length=120)),
                ("description", models.TextField(blank=True)),
                ("criteres_evaluation", models.TextField(blank=True, help_text="Critères utilisés par le directeur pour évaluer les auditions.")),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                ("scenario", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="roles", to="casting.scenario")),
            ],
            options={"ordering": ["titre"], "unique_together": {("scenario", "titre")}},
        ),
    ]
