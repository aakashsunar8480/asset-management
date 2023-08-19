import graphene


class UserStatusEnum(graphene.Enum):

    ACTIVE = 'active'
    INACTIVE = 'inactive'