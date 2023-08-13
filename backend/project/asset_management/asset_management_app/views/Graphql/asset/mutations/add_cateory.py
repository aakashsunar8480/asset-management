import graphene

from ..types.category_type import CategoryType
from asset_management_app.models.Assets import Category
from ...core.model_mutation import ModelMutation


class AddCategoryInput(graphene.InputObjectType):
    name = graphene.String(required=True, description="Name of the category")
    description = graphene.String(description="description of the category")


class AddCategory(ModelMutation):
    category = graphene.Field(CategoryType)

    class Meta:
        model = Category

    class Arguments:
        input = AddCategoryInput()
