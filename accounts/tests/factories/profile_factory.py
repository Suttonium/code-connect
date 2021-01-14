import factory

from faker import Factory

from accounts.models.profile               import Profile
from accounts.tests.factories.user_factory import UserFactory

faker = Factory.create()


class ProfileFactory(factory.django.DjangoModelFactory):

    class Meta:
        model                = Profile
        django_get_or_create = (
            'user',
        )

    user = factory.SubFactory(UserFactory)
