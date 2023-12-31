"""LoginUser mutation."""
from typing import Any

import graphene
from django.contrib.auth import authenticate
from graphql import GraphQLError
from graphql_jwt.refresh_token.shortcuts import create_refresh_token
from graphql_jwt.shortcuts import get_token

from ..types.login_user_type import LoginUserType


class LoginUser(graphene.Mutation):
    """LoginUser mutation."""

    login_user = graphene.Field(LoginUserType)

    class Arguments:
        """LoginUser Arguments."""

        username = graphene.String(required=True)
        password = graphene.String(required=True)

    @classmethod
    def mutate(cls: Any, root: Any, info: Any, username: str, password: str) -> Any:
        """Mutate method for LoginUser."""
        user = authenticate(username=username, password=password)
        if user:
            access_token = get_token(user)
            refresh_token = create_refresh_token(user)
            login_user = LoginUserType(
                user=user, access_token=access_token, refresh_token=refresh_token
            )
            return LoginUser(login_user=login_user)
        raise GraphQLError("Invalid credentials")
