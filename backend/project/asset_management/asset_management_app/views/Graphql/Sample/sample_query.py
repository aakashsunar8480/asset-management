import graphene
from graphql import GraphQLError


class SampleQueryResult(graphene.ObjectType):
    message = graphene.String()


class SampleQueryResolver:
    @staticmethod
    def resolve(parent, info, name):
        request = info.context
        if hasattr(request, "access_token_payload"):
            return SampleQueryResult(message=f"Hello {name} !!!!")
        raise GraphQLError(message="Anonymous user")


class SampleQuery(graphene.ObjectType):
    hello = graphene.Field(
        SampleQueryResult,
        name=graphene.String(description="Your name"),
        resolver=SampleQueryResolver.resolve,
    )
