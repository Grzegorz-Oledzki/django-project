# Generated by Django 3.2.9 on 2022-03-14 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("first_project", "0006_auto_20220309_1956"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="player",
            options={"ordering": ["-vote_ratio", "-vote_total", "title"]},
        ),
    ]
