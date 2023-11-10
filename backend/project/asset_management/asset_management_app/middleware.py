"""Custom middleware to authenticate the API headers."""

from typing import Any, Callable

from django.http import HttpRequest
from graphql import GraphQLError
from graphql_jwt.utils import jwt_decode

ALLOWED_MUTATION = ["loginUser", "createUser"]


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
            except Exception as error:
                raise GraphQLError(f"Anonymous user :-{error}")
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
                if selection_name not in ALLOWED_MUTATION:
                    raise GraphQLError(f"Permission denied for:-{selection_name}")
        return next(root, info, **kwargs)
