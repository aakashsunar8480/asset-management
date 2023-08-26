"""UpdateUserStatus mutation."""
from typing import Any

import graphene
from asset_management_app.enums.users.user_status_enum import UserStatusEnum
from django.contrib.auth.models import User
from graphql import GraphQLError


class UpdateUserStatus(graphene.Mutation):
    """UpdateUserStatus mutation."""

    success = graphene.Boolean()
    message = graphene.String()

    status_map = {
        UserStatusEnum.ACTIVE: (True, "activated"),
        UserStatusEnum.INACTIVE: (False, "deactivated"),
    }

    class Arguments:
        """UpdateUserStatus Arguments."""

        username = graphene.String(required=True)
        status = graphene.Argument(UserStatusEnum, required=True)

    @classmethod
    def mutate(
        cls: Any, root: Any, info: Any, username: str, status: UserStatusEnum
    ) -> Any:
        """Mutate method for UpdateUserStatus."""
        request = info.context
        if hasattr(request, "access_token_payload"):
            user = User.objects.get(username=username)
            if user:
                user_status, action = cls.status_map[status]
                user.is_active = user_status
                user.save()
                return UpdateUserStatus(
                    success=True, message=f"User {username} has been {action}."
                )
            return UpdateUserStatus(
                success=False, message=f"User {username} not found."
            )
        raise GraphQLError(message="Anonymous user")
