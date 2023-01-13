# Generated by Django 4.1.5 on 2023-01-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("idiosaneapp", "0007_article_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="summary",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="Title",
            field=models.CharField(max_length=10000),
        ),
    ]
