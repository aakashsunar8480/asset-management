"""Asset view schema."""
import graphene

from .mutations.add_cateory import AddCategory


class Mutations(graphene.ObjectType):
    """Asset view mutations."""

    add_category = AddCategory.Field()
