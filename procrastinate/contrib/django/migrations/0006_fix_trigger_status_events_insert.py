# Generated by Django 3.1 on 2020-08-22 16:57

from django.db import migrations

import procrastinate.contrib.django


class Migration(migrations.Migration):

    dependencies = [
        ("procrastinate", "0005_fix_procrastinate_fetch_job"),
    ]

    operations = [
        procrastinate.contrib.django.RunProcrastinateFile(
            filename="delta_0.7.1_001_fix_trigger_status_events_insert.sql",
        ),
    ]
