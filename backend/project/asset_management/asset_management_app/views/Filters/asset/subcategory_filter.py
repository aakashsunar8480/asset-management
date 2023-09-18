"""Subcategory model filters."""
from typing import Any

from django.db.models import Q


class SubcategoryFilter:
    """Subcategory model filters."""

    @classmethod
    def build_filter_from_criteria(cls: Any, criteria: dict) -> Any:
        """Build filter."""
        custom_filter = Q()
        for key in criteria.keys():
            item = criteria.get(key)
            custom_filter = custom_filter & Q(
                **{f"subcategory__{key}__{item.get('operation')}": item.get("value")}
            )
        return custom_filter
