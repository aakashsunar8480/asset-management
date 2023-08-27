"""Asset view schema."""
import graphene

from .mutations.add_cateory import AddCategory
from .resolvers.search_resolver import SearchResolver
from .types.search_result_type import SearchResultType


class Mutations(graphene.ObjectType):
    """Asset view mutations."""

    add_category = AddCategory.Field()


class Queries(graphene.ObjectType):
    """Asset view Queries."""

    search = graphene.List(
        SearchResultType, criteria=graphene.String(), resolver=SearchResolver.resolve
    )
