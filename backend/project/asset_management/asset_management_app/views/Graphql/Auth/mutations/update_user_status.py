import graphene
from asset_management_app.enums.users.user_status_enum import UserStatusEnum
from django.contrib.auth.models import User
from graphql import GraphQLError


class UpdateUserStatus(graphene.Mutation):
    success = graphene.Boolean()
    message = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        status = graphene.Argument(UserStatusEnum, required=True)

    def mutate(self, info, username, status):
        request = info.context
        if hasattr(request, 'access_token_payload'):
            user = User.objects.get(username=username)
            if user:
                if status == UserStatusEnum.ACTIVE:
                    user.is_active = True
                    action = "activated"
                else:
                    user.is_active = False
                    action = "deactivated"
                user.save()
                return UpdateUserStatus(success=True, message=f"User {username} has been {action}.")
            return UpdateUserStatus(success=False, message=f"User {username} not found.")
        raise GraphQLError(message="Anonymous user")