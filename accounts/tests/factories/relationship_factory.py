import factory

from faker import Factory

from accounts.models.relationship          import Relationship
from accounts.tests.factories.user_factory import UserFactory

faker = Factory.create()


class RelationshipFactory(factory.django.DjangoModelFactory):


    class Meta:
        model                = Relationship
        django_get_or_create = (
            'sender',
            'receiver'
        )

    sender   = factory.SubFactory(UserFactory)
    receiver = factory.SubFactory(UserFactory)
