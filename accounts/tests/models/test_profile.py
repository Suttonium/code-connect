import logging

from django.test import TestCase
from typing      import Optional

from accounts.exception                       import AccountsException
from accounts.models.profile                  import Profile
from accounts.tests.factories.profile_factory import ProfileFactory

logger = logging.getLogger('accounts.tests')


class TestProfile(TestCase):

    _test_profile: Optional[Profile] = None
    _test_name   : Optional[str]     = None

    def setUp(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The setUp method generates the test profile used in the
        undermentioned methods.
        """
        try:
            self._test_profile = ProfileFactory()
        except Exception as error:
            logger.exception('Failed Test Profile Initialization')
            self.fail()

    def test_profile_is_connected_to_a_user(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_profile_is_connected_to_a_user method assures that when the
        user was created, an associated Profile instance was also created.
        """
        self._test_name = 'Test Profile is Connceted to a User'
        try:
            self.assertIsNotNone(
                self._test_profile.user
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #1 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #1 - {self._test_name}')

    def test_gender_default_is_prefer_not_to_say(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_gender_default_is_prefer_not_to_say method assures
        a user's gender is defaulted to PREFER_NOT_TO_SAY.
        """
        self._test_name = 'Test Gender Default is Prefer Not to Say'
        try:
            self.assertEqual(
                self._test_profile.gender,
                Profile.GenderOptions.PREFER_NOT_TO_SAY
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #2 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #2 - {self._test_name}')

    def test_uuid_label(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_uuid_label method validates the label used when
        displaying the UUID on the frontend.
        """
        self._test_name = 'Test UUID Label'
        try:
            self.assertEqual(
                'UUID',
                self._test_profile._meta.get_field('uuid').verbose_name
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #3 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #3 - {self._test_name}')

    def test_gender_label(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_gender_label method validates the label used when
        displaying the Gender on the frontend.
        """
        self._test_name = 'Test Gender Label'
        try:
            self.assertEqual(
                'Gender',
                self._test_profile._meta.get_field('gender').verbose_name
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #4 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #4 - {self._test_name}')
