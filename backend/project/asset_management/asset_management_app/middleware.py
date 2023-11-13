"""Custom middleware to authenticate the API headers."""

from typing import Any, Callable

from django.http import HttpRequest, JsonResponse
from graphql import GraphQLError
from graphql_jwt.utils import jwt_decode

ALLOWED_OPERATIONS = {
    "mutation": ["loginUser", "createUser"],
    "query": ["__schema", None],
}


def check_authentication(selection_name: Any, allowed_operation: list) -> None:
    """Check allowed operations."""
    if selection_name not in allowed_operation:
        raise GraphQLError(f"Permission denied for:-{selection_name}")


class VerifyAccessTokenMiddleware:
    """Authenticates access token."""

    def __init__(self: Any, get_response: Callable[[HttpRequest], Any]) -> None:
        """Initialize the get_response function."""
        self.get_response = get_response

    def __call__(self: Any, request: HttpRequest) -> Any:
        """Authenticate access token using GraphQL JWT."""
        auth_header = request.META.get("HTTP_AUTHORIZATION", "")
        if auth_header.startswith("Bearer "):
            access_token = auth_header[7:]
            try:
                decoded_payload = jwt_decode(access_token)
                # Attach the decoded payload to the request
                request.access_token_payload = decoded_payload
            except Exception:
                return JsonResponse(
                    {
                        "error": {
                            "message": "Access token expired or invalid.",
                            "code": "401",
                        }
                    }
                )
        return self.get_response(request)


class AuthenticationMiddleware:
    """Authentication middleware for all graphql operations."""

    @staticmethod
    def resolve(next: Callable, root: Any, info: Any, **kwargs: dict) -> Callable:
        """Authenticate user and allowed mutations."""
        context = info.context
        if not hasattr(context, "access_token_payload"):
            for selection in info.operation.selection_set.selections:
                selection_name = str(selection.name.value)
                check_authentication(
                    selection_name,
                    ALLOWED_OPERATIONS.get(info.operation.operation.value),
                )
        return next(root, info, **kwargs)
