import logging

from django.test import TestCase
from typing      import Optional

from accounts.exception                       import AccountsException
from accounts.models.profile                  import Profile
from accounts.tests.factories.profile_factory import ProfileFactory

logger = logging.getLogger('accounts.tests')


class TestProfile(TestCase):
    _test_profile : Optional[Profile] = None

    def setUp(self) -> None:
        try:
            self._test_profile = ProfileFactory()
        except AccountsException as error:
            logger.exception('Failed Test Profile Initialization')
            self.fail()

    def test_profile_is_connected_to_a_user(self) -> None:
        try:
            self.assertIsNotNone(self._test_profile.user)
        except AssertionError as error:
            logger.exception('Failed Test #1 - Test Profile is Connected to a User')
            self.fail()
        else:
            logger.info('Completed Test #1 - Test Profile is Connected to a User')

    def test_gender_default_is_prefer_not_to_say(self) -> None:
        try:
            self.assertEqual(self._test_profile.gender, Profile.GenderOptions.PREFER_NOT_TO_SAY)
        except AssertionError as error:
            logger.exception('Failed Test #2 - Test Gender Default is Prefer Not to Say')
            self.fail()
        else:
            logger.info('Completed Test #2 - Test Gender Default is Prefer Not to Say')
