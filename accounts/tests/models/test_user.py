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
    The TestUser class handles any necessary testing of the user model.
    This class is designed to handle incorrect and correct test results by
    logging success and failure messages.
    """

    _test_user: Optional[User] = None
    _test_name: Optional[str]  = None

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
        self._test_name = 'Test is_banned Default is False'
        try:
            self.assertFalse(self._test_user.is_banned)
        except AssertionError as error:
            logger.exception(f'Failed Test #1 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #1 - {self._test_name}')

    def test_emails_are_unique(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_emails_are_unique method attempts to create a user with an email
        equal to the user created in setUp.
        """
        self._test_name = 'Test Emails are Unique'
        try:
            User.create_user(
                email=self._test_user.email,
                username='Test User #2',
                password='test password'
            )
        except IntegrityError as error:
            logger.info(f'Completed Test #2 - {self._test_name}')
        else:
            logger.exception(f'Failed Test #2  - {self._test_name}')
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
        self._test_name = 'Test UUID Field is Generated'
        try:
            self.assertIsNotNone(self._test_user.uuid)
        except AssertionError as error:
            logger.exception(f'Failed Test #3 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #3 - {self._test_name}')

    def test_profile_instance_is_created(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_profile_object_is_created method assures a profile instance is
        connected to the user instance upon creation.
        """
        self._test_name = 'Test Profile Instance is Created'
        try:
            self.assertIsNotNone(self._test_user.profile)
        except AssertionError as error:
            logger.exception(f'Failed Test #4 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #4 - {self._test_name}')

    def test_uuid_label(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_uuid_label method validates the UUID labeled that would
        be displayed on the frontend.
        """
        self._test_name = 'Test UUID Label'
        try:
            self.assertEqual(
                'UUID',
                 self._test_user._meta.get_field('uuid').verbose_name
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #5 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #5 - {self._test_name}')

    def test_email_label(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_email_label method validates the label used when displaying
        the email field on the frontend.
        """
        self._test_name = 'Test Email Label'
        try:
            self.assertEqual(
                'Email Address',
                 self._test_user._meta.get_field('email').verbose_name
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #6 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #6 - {self._test_name}')

    def test_is_banned_label(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_is_banned_label method validates the label used for the
        is_banned status when/if it is ever displayed on the frontend.
        """
        self._test_name = 'Test is_banned Label'
        try:
            self.assertEqual(
                'Banned Status',
                 self._test_user._meta.get_field('is_banned').verbose_name
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #7 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #7 - {self._test_name}')

    def test_string_representation_equals_email_address(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_string_representation_equals_email_address method assures
        the email address is returned when stringifying the user instance.
        """
        self._test_name = 'Test String Representatiion Equals Email Address'
        try:
            self.assertEqual(
                str(self._test_user),
                self._test_user.email
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #8 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #8 - {self._test_name}')

    def test_banning_a_user(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_banning_a_user method validates a user's banned status
        after banning the user from the application.
        """
        self._test_name = 'Test Banning a User'
        try:
            self._test_user.ban()
            self.assertTrue(
                self._test_user.is_banned
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #9 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #9 - {self._test_name}')

    def test_unbanning_a_user(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_unbanning_a_user method validates a user's banned status
        after unbanning the user from the application.
        """
        self._test_name = 'Test Unbanning a User'
        try:
            self._test_user.unban()
            self.assertFalse(
                self._test_user.is_banned
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #10 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #10 - {self._test_name}')

