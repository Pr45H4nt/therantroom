# Generated by Django 4.1.5 on 2023-01-13 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("idiosaneapp", "0009_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=100)),
                ("Email", models.EmailField(max_length=254)),
                ("Message", models.TextField()),
            ],
        ),
    ]