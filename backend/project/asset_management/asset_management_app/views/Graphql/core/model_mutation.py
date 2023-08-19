import graphene
from graphene.types.mutation import MutationOptions


def get_model_name(model):
    """Return name of the model with first letter lowercase."""
    model_name = model.__name__
    return model_name[:1].lower() + model_name[1:]


class ModelMutationOptions(MutationOptions):
    """Model mutation meta options."""

    exclude = None  # Tuple or list of fields to exclude during object full_clean
    model = None  # Django Model for which the mutation is created.
    return_field_name = None


class ModelMutation(graphene.Mutation):

    class Meta:
        abstract = True

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        model=None,
        model_type=None,
        exclude=None,
        arguments=None,
        **options,
    ) :
        """Initialize the model mutation with meta information."""
        if not model:
            raise Exception("model not found.")

        _meta = ModelMutationOptions(cls)

        if exclude is None:
            exclude = []

        return_field_name = get_model_name(model)

        _meta.model = model
        _meta.return_field_name = return_field_name
        _meta.exclude = exclude
        super().__init_subclass_with_meta__(description="description", _meta=_meta, **options)

    @classmethod
    def get_model(cls):
        return cls._meta.model

    @classmethod
    def _save(cls, instance):
        instance.save()

    @classmethod
    def _clean_input(cls,model,**data):
        instance = model(**data)
        return instance

    @classmethod
    def _post_save(cls):
        pass

    @classmethod
    def _get_result(cls,instance):
        return cls(instance)

    @classmethod
    def mutate(cls, root, info, **data):
        try:
            model = cls.get_model()
            instance = cls._clean_input(model, **data.get("input"))
            cls._save(instance)
            cls._post_save()
            success_response = cls._get_result(instance)
            return success_response
        except Exception as ex:
            raise ex
