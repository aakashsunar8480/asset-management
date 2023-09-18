"""Schema for asset_management_app."""
import graphene
from asset_management_app.views.Graphql.Sample.sample_query import SampleQuery

from .asset import schema as AssetSchema
from .Auth import schema as AuthSchema


class Mutation(AuthSchema.Mutations, AssetSchema.Mutations):
    """All the Mutation in view will be inherited here."""

    pass


class Query(SampleQuery, AssetSchema.Queries):
    """All the queries in view will be inherited here."""

    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
