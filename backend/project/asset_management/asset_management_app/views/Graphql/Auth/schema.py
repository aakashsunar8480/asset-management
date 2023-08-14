import graphene

from asset_management_app.views.Graphql.Auth.mutations.access_token_by_refresh_token import AccessTokenByRefreshToken
from asset_management_app.views.Graphql.Auth.mutations.create_user import CreateUser
from asset_management_app.views.Graphql.Auth.mutations.user_login import LoginUser


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    login_user = LoginUser.Field()
    access_token_by_refresh_token = AccessTokenByRefreshToken.Field()