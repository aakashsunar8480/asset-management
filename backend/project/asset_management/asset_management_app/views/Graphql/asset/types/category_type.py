from graphene_django.types import DjangoObjectType
from asset_management_app.models.Assets import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
