# Generated by Django 3.2.9 on 2022-01-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("first_project", "0002_auto_20220110_2120"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="featured_image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to=""
            ),
        ),
    ]
