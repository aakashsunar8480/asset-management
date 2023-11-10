"""Asset search resolver."""
import json
from typing import Any

from asset_management_app.views.Filters.base_filter import BaseFilters


class SearchResolver:
    """Asset search resolver."""

    @staticmethod
    def resolve(root: Any, info: Any, criteria: str) -> Any:
        """Search query resolver."""
        criteria = json.loads(criteria)
        return BaseFilters.get_criteria_result(criteria)
