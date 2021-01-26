import logging

from django.db   import IntegrityError
from django.test import TestCase
from typing      import Optional

from accounts.exception                    import AccountsException
from accounts.models.user                  import User
from accounts.tests.factories.user_factory import UserFactory

logger = logging.getLogger('accounts.tests')


class TestUser(TestCase):
    """
    The UserTest class handles any necessary testing of the user model.
    This class is designed to handle incorrect and correct test results by
    logging success and failure messages.
    """

    _test_user: Optional[User] = None

    def setUp(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The setUp method generates the test user used in the
        undermentioned methods.
        """
        try:
            self._test_user = UserFactory()
        except AccountsException as error:
            logger.exception('Failed Initialization of the Test Class')
            self.fail()

    def test_is_banned_default_is_false(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_is_banned_default_is_false checks if the is_banned
        field is set to False by default when a User instance is created.
        """
        try:
            self.assertFalse(self._test_user.is_banned)
        except AssertionError as error:
            logger.exception('Failed Test #1 - Test is_banned Default is False')
            self.fail()
        else:
            logger.info('Completed Test #1 - Test is_banned Default is False')

    def test_emails_are_unique(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_emails_are_unique method attempts to create a user with an email
        equal to the user created in setUp.
        """
        try:
            User.objects.create(
                email=self._test_user.email,
                username='Test User #2'
            )
        except IntegrityError as error:
            logger.info('Completed Test #2 - Test Emails Are Unique')
        else:
            logger.exception('Failed Test #2  - Test Emails Are Unique')
            self.fail()

    def test_uuid_field_is_generated(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_uuid_field_is_generated method checks to see if a UUID is 
        assigned to a User instance upon creation.
        """
        try:
            self.assertIsNotNone(self._test_user.uuid)
        except AssertionError as error:
            logger.exception('Failed Test #3 - Test UUID Field is Generated')
            self.fail()
        else:
            logger.info('Completed Test #3 - Test UUID Field is Generated')

    def test_profile_instance_is_created(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_profile_object_is_created method assures a profile instance is
        connected to the user instance upon creation.
        """
        try:
            self.assertIsNotNone(self._test_user.profile)
        except AssertionError as error:
            logger.exception('Failed Test #4 - Test Profile Instance is Created')
            self.fail()
        else:
            logger.info('Completed Test #4 - Test Profile Instance is Created')

    def test_uuid_label(self) -> None:
        try:
            self.assertEqual(
                'UUID',
                 self._test_user._meta.get_field('uuid').verbose_name
            )
        except AssertionError as error:
            logger.exception('Failed Test #5 - Test uuid Label')
            self.fail()
        else:
            logger.info('Completed Test #5 - Test uuid Label')

    def test_email_label(self) -> None:
        try:
            self.assertEqual(
                'Email Address',
                 self._test_user._meta.get_field('email').verbose_name
            )
        except AssertionError as error:
            logger.exception('Failed Test #6 - Test email Label')
            self.fail()
        else:
            logger.info('Completed Test #6 - Test email Label')

    def test_is_banned_label(self) -> None:
        try:
            self.assertEqual(
                'Banned Status',
                 self._test_user._meta.get_field('is_banned').verbose_name
            )
        except AssertionError as error:
            logger.exception('Failed Test #7 - Test is_banned Label')
            self.fail()
        else:
            logger.info('Completed Test #7 - Test is_banned Label')

    def test_string_representation_equals_email_address(self) -> None:
        try:
            self.assertEqual(
                str(self._test_user),
                self._test_user.email
            )
        except AssertionError as error:
            logger.exception('Failed Test #8 - Test String Representation Equals Email Address')
            self.fail()
        else:
            logger.info('Completed Test #8 - Test String Representation Equals Email Address')

