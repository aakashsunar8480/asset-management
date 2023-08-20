# Generated by Django 4.2.4 on 2023-08-12 05:57

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False,
                        help_text="Flag representing if object is set to be deleted.",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Timestamp at which this object was deleted.",
                        null=True,
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.CharField(max_length=300)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False,
                        help_text="Flag representing if object is set to be deleted.",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Timestamp at which this object was deleted.",
                        null=True,
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Vendors",
            fields=[
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False,
                        help_text="Flag representing if object is set to be deleted.",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Timestamp at which this object was deleted.",
                        null=True,
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("mobile", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254)),
                ("description", models.CharField(max_length=200)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Warranty",
            fields=[
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False,
                        help_text="Flag representing if object is set to be deleted.",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Timestamp at which this object was deleted.",
                        null=True,
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("warranty_type", models.CharField(max_length=100)),
                ("duration", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SubCategory",
            fields=[
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False,
                        help_text="Flag representing if object is set to be deleted.",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Timestamp at which this object was deleted.",
                        null=True,
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
                ("description", models.CharField(max_length=300)),
                ("model", models.CharField(max_length=200, unique=True)),
                ("host_name", models.CharField(max_length=200, unique=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="asset_management_app.category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Employees",
            fields=[
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False,
                        help_text="Flag representing if object is set to be deleted.",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Timestamp at which this object was deleted.",
                        null=True,
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("emp_id", models.CharField(max_length=20, unique=True)),
                ("email", models.EmailField(max_length=100)),
                ("mobile", models.CharField(max_length=10, unique=True)),
                (
                    "user_type",
                    models.CharField(
                        choices=[
                            ("Employed", "EMPLOYED"),
                            ("Contractor", "CONTRACTOR"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Active", "ACTIVE"),
                            ("On Leave", "ON_LEAVE"),
                            ("Terminated", "TERMINATED"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="asset_management_app.organization",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Assets",
            fields=[
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False,
                        help_text="Flag representing if object is set to be deleted.",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Timestamp at which this object was deleted.",
                        null=True,
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("asset_id", models.CharField(max_length=200, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Available", "AVAILABLE"),
                            ("In Use", "IN_USE"),
                            ("Maintenance", "MAINTENANCE"),
                            ("Lost", "LOST"),
                            ("Retired", "RETIRED"),
                        ],
                        max_length=20,
                    ),
                ),
                ("primary_owner", models.CharField()),
                ("purchase_date", models.DateField()),
                (
                    "employees",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="asset_management_app.employees",
                    ),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="asset_management_app.subcategory",
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="asset_management_app.vendors",
                    ),
                ),
                (
                    "warranty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="asset_management_app.warranty",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
