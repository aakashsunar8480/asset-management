"""UserType."""
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    """UserType."""

    class Meta:
        """UserType meta."""

        model = User
