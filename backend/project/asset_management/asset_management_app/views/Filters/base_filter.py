"""Base filters."""
from typing import Any

from asset_management_app.models.Assets import Assets
from asset_management_app.views.Filters.asset.asset_filter import AssetFilter
from asset_management_app.views.Filters.asset.subcategory_filter import (
    SubcategoryFilter,
)
from django.db.models import Q
from graphql import GraphQLError


class BaseFilters:
    """Base filters."""

    CRITERIA_MAP = {"asset": AssetFilter, "subcategory": SubcategoryFilter}

    @classmethod
    def get_criteria_result(cls: Any, criteria: dict) -> Any:
        """Build criteria and result."""
        try:
            custom_filter = Q()
            for key in criteria.keys():
                custom_filter = custom_filter & cls.CRITERIA_MAP[
                    key
                ].build_filter_from_criteria(criteria[key])

            result = Assets.objects.filter(custom_filter)

            return result
        except Exception as e:
            raise GraphQLError(message=f"Invalid key./n {e}")
