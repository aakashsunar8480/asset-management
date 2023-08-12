import graphene


class SampleQueryResult(graphene.ObjectType):
    message = graphene.String()


class SampleQueryResolver:

    @staticmethod
    def resolve(parent,info,name):
        print(parent,info)
        return SampleQueryResult(message=f'Hello {name} !!!!')


class SampleQuery(graphene.ObjectType):
    hello = graphene.Field(
        SampleQueryResult,
        name=graphene.String(description="Your name"),
        resolver=SampleQueryResolver.resolve
    )
