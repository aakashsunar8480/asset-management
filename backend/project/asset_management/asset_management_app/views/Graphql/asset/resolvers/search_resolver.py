"""Asset search resolver."""
import json
from typing import Any

from asset_management_app.views.Filters.base_filter import BaseFilters
from graphql import GraphQLError


class SearchResolver:
    """Asset search resolver."""

    @staticmethod
    def resolve(root: Any, info: Any, criteria: str) -> Any:
        """Search query resolver."""
        request = info.context
        if hasattr(request, "access_token_payload"):
            criteria = json.loads(criteria)
            return BaseFilters.get_criteria_result(criteria)
        raise GraphQLError(message="Anonymous user")
