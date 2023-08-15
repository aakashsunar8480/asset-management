# Generated by Django 4.2.4 on 2023-08-15 07:46

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assets',
            name='warranty',
        ),
        migrations.AddField(
            model_name='assets',
            name='warranty_end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='warranty_start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='warranty_type',
            field=models.CharField(choices=[('Partial', 'PARTIAL'), ('Full', 'FULL')], default="FULL", max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Warranty',
        ),
    ]
