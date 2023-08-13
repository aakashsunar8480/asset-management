import graphene
from asset_management_app.views.Graphql.Sample.sample_query import SampleQuery
from .Auth import schema as AuthSchema
class Mutation(AuthSchema.Mutation):
    """
    All the Mutation in view will be inherited here.
    """
    pass



class Query(SampleQuery):
    """
    All the queries in view will be inherited here.
    """
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
