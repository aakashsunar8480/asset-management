"""CreateUser mutation."""
from typing import Any

import graphene
from django.contrib.auth.models import User
from graphql import GraphQLError

from ..types.user_type import UserType


class CreateUser(graphene.Mutation):
    """CreateUser mutation."""

    user = graphene.Field(UserType)

    class Arguments:
        """CreateUser Arguments."""

        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    @classmethod
    def mutate(
        cls: Any, root: Any, info: Any, username: str, email: str, password: str
    ) -> Any:
        """Mutate method for CreateUser."""
        request = info.context
        if hasattr(request, "access_token_payload"):
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            user.save()
            return CreateUser(user=user)
        raise GraphQLError(message="Anonymous user")
