import graphene
from django.contrib.auth.models import User
from graphql import GraphQLError

from ..types.user_type import UserType


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, username, email, password):
        request = info.context
        if hasattr(request, "access_token_payload"):
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            user.save()
            return CreateUser(user=user)
        raise GraphQLError(message="Anonymous user")
