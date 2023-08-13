import graphene
from asset_management_app.views.Graphql.Auth.mutations.create_user import CreateUser
from asset_management_app.views.Graphql.Auth.mutations.user_login import LoginUser

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login_user = LoginUser.Field()