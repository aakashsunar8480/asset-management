"""AddSubCategory mutation."""
from typing import Any

import graphene
from asset_management_app.models.Assets import Category, SubCategory

from ...core.model_mutation import ModelMutation
from ..types.sub_category_type import SubCategoryType


class AddSubCategoryInput(graphene.InputObjectType):
    """AddSubCategory input type."""

    name = graphene.String(required=True, description="Name of the subcategory")
    category = graphene.ID(description="ID of the category")
    description = graphene.String(description="description of the subcategory")
    model = graphene.String(description="Model of the subcategory")
    host_name = graphene.String(description="Host name  of the device")


class AddSubCategory(ModelMutation):
    """AddSubCategory mutation."""

    subcategory = graphene.Field(SubCategoryType)

    class Meta:
        """AddSubCategory meta."""

        model = SubCategory

    class Arguments:
        """AddSubCategory Arguments."""

        input = AddSubCategoryInput()

    @classmethod
    def _clean_input(cls: Any, **data: dict) -> Any:
        """Input formatting and instance creation."""
        model = cls.get_model()
        data["category"] = Category.objects.get(id=data["category"])
        instance = model(**data)
        return instance
