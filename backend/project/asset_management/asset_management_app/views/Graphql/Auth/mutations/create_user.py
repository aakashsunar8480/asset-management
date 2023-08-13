import graphene
from django.contrib.auth.models import User
from ..types.user_type import UserType
class CreateUser(graphene.Mutation):
    user=graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, email, password):
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return CreateUser(user=user)