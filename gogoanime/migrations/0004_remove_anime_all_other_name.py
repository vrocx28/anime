# Generated by Django 4.1.1 on 2022-12-27 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gogoanime", "0003_anime_all_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="anime_all",
            name="other_name",
        ),
    ]