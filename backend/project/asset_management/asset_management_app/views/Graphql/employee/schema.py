"""Employee view schema."""
import graphene

from .mutations.add_employee import AddEmployee
from .mutations.add_organization import AddOrganization


class Mutations(graphene.ObjectType):
    """Employee view mutations."""

    add_organization = AddOrganization.Field()
    add_employee = AddEmployee.Field()
