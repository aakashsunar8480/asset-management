"""SampleQuery."""
from typing import Any

import graphene
from graphql import GraphQLError


class SampleQueryResult(graphene.ObjectType):
    """SampleQuery return type."""

    message = graphene.String()


class SampleQueryResolver:
    """SampleQuery resolver."""

    @staticmethod
    def resolve(parent: Any, info: Any, name: str) -> Any:
        """Query resolver."""
        request = info.context
        if hasattr(request, "access_token_payload"):
            return SampleQueryResult(message=f"Hello {name} !!!!")
        raise GraphQLError(message="Anonymous user")


class SampleQuery(graphene.ObjectType):
    """SampleQuery."""

    hello = graphene.Field(
        SampleQueryResult,
        name=graphene.String(description="Your name"),
        resolver=SampleQueryResolver.resolve,
    )
