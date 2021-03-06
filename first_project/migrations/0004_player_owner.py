# Generated by Django 3.2.9 on 2022-01-24 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_profile_username"),
        ("first_project", "0003_player_featured_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.profile",
            ),
        ),
    ]
