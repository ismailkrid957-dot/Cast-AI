from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("casting", "0002_role"),
        ("evaluations", "0002_evaluation"),
    ]
    operations = [
        migrations.AddField(
            model_name="audition",
            name="role",
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="auditions", to="casting.role"),
        ),
    ]
