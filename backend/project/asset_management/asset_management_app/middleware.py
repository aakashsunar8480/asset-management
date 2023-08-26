"""Custom middleware to authenticate the API headers."""

from typing import Any, Callable

from django.http import HttpRequest
from graphql import GraphQLError
from graphql_jwt.utils import jwt_decode


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
