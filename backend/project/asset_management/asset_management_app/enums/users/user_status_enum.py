"""User status enum."""
import graphene


class UserStatusEnum(graphene.Enum):
    """User status enum."""

    ACTIVE = "active"
    INACTIVE = "inactive"
