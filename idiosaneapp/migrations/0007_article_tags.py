# Generated by Django 4.1.5 on 2023-01-10 15:48

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("idiosaneapp", "0006_alter_article_poster"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="Tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
