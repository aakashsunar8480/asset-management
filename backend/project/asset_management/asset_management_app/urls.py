from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

from asset_management_app.views.Graphql import api

urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(schema=api.schema,graphiql=True))),
]