import graphene

from asset_management_app.views.Graphql.Sample.sample_query import SampleQuery


# class Mutation():
#     """
#     All the Mutation in view will be inherited here.
#     """
#     pass


class Query(SampleQuery):
    """
    All the queries in view will be inherited here.
    """
    pass


schema = graphene.Schema(query=Query)
