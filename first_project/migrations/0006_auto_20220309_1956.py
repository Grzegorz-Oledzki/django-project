# Generated by Django 3.2.9 on 2022-03-09 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_auto_20220126_1841"),
        ("first_project", "0005_auto_20220303_1951"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="project",
            new_name="player",
        ),
        migrations.AlterUniqueTogether(
            name="review",
            unique_together={("owner", "player")},
        ),
    ]
