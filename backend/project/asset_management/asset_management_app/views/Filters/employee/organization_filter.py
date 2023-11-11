"""Organization model filters."""
from typing import Any

from django.db.models import Q


class OrganizationFilter:
    """Organization model filters."""

    @classmethod
    def build_filter_from_criteria(cls: Any, criteria: dict) -> Any:
        """Build filter."""
        custom_filter = Q()
        for key in criteria.keys():
            custom_filter = custom_filter & Q(
                **{f"employees__organization__{key}__icontains": criteria.get(key)}
            )
        return custom_filter