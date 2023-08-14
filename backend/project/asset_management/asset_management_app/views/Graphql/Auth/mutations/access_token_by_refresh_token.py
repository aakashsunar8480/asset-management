import graphene
from graphql_jwt.shortcuts import  get_token, get_refresh_token
from graphql import GraphQLError


class AccessTokenByRefreshToken(graphene.Mutation):
    access_token = graphene.String()

    class Arguments:
        refresh_token = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, refresh_token):
        refresh_token_instance = get_refresh_token(refresh_token)
        if refresh_token_instance.user:
            access_token = get_token(refresh_token_instance.user)
            return AccessTokenByRefreshToken(access_token=access_token)
        else:
            raise GraphQLError(message="Invalid refresh token")
