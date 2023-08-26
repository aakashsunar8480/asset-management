"""Application config."""
from django.apps import AppConfig


class AssetManagementAppConfig(AppConfig):
    """Asset management app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "asset_management_app"
