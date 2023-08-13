import graphene
from .mutations.add_cateory import AddCategory


class Mutations(graphene.ObjectType):
    add_category = AddCategory.Field()
