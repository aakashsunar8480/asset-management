import graphene
from .user_type import UserType

class LoginUserType(graphene.ObjectType):
    user = graphene.Field(UserType)
    access_token = graphene.String()
    refresh_token = graphene.String()