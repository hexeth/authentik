# Generated by Django 3.2.1 on 2021-05-05 17:17

import django.contrib.postgres.fields
from django.db import migrations, models

import authentik.lib.generators


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_sources_plex", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="plexsource",
            name="allow_friends",
            field=models.BooleanField(
                default=True,
                help_text="Allow friends to authenticate, even if you don't share a server.",
            ),
        ),
        migrations.AddField(
            model_name="plexsource",
            name="plex_token",
            field=models.TextField(default="", help_text="Plex token used to check friends"),
        ),
        migrations.AlterField(
            model_name="plexsource",
            name="allowed_servers",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.TextField(),
                blank=True,
                default=list,
                help_text="Which servers a user has to be a member of to be granted access. Empty list allows every server.",
                size=None,
            ),
        ),
    ]
