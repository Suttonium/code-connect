import factory

from faker import Factory

from accounts.models.user import User

faker = Factory.create()


class UserFactory(factory.django.DjangoModelFactory):
    """
    The UserFactory class will simplify making User instances
    during the execution of test cases.
    """

    class Meta:
        """
        The UserFactory.Meta class handles associating the User class
        to the UserFactory class and handling getting or creating usernames
        and email addresses.
        """
        model                = User
        django_get_or_create = (
            'username',
            'email'
        )

    username = factory.Sequence(lambda n: 'user_%d' % n)
    email    = faker.email()
