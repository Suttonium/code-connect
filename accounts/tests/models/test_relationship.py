import logging

from django.conf import settings
from django.test import TestCase
from typing      import Optional

from accounts.models.relationship                  import Relationship
from accounts.tests.factories.relationship_factory import RelationshipFactory

logger = logging.getLogger('accounts.tests')


class TestRelationship(TestCase):
    """
    The TestRelationship class handles any necessary testing of the relationship model.
    This class is designed to hangle incorrect and correct test reults by
    logging success and failure messages.
    """

    _test_relationship: Optional[Relationship] = None
    _test_name        : Optional[str]          = None

    def setUp(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The setUp method generates the test relationship used in the
        undermentioned methods
        """
        try:
            self._test_relationship = RelationshipFactory()
        except Exception as error:
            logger.exception('Failed Initialization of the Test Class')
            self.fail()

    def test_uuid_is_generated_upon_instance_creation(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_uuid_is_generated_upon_instance_creation method checks if a
        valid uuid is created during the relationship instance's creation.
        """
        self._test_name = "Test UUID is Generated Upon Instance Creation"
        try:
            self.assertIsNotNone(self._test_relationship.uuid)
        except AssertionError as error:
            logger.exception(f'Failed Test #1 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #1 - {self._test_name}')

    def test_sender_is_not_none_upon_instance_creation(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_sender_is_not_none_upon_instance_creation method checks if
        the sender of the relationship request is correctly assigned to the
        model instance.
        """
        self._test_name = "Test Sender is not None Upon Instance Creation"
        try:
            self.assertIsNotNone(self._test_relationship.sender)
        except AssertionError as error:
            logger.exception(f'Failed Test #2 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #2 - {self._test_name}')

    def test_receiver_is_not_none_upon_instance_creation(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_receiver_is_not_none_upon_instance_creation method checks if
        the receiver of the relationship request is correctly assigned to the
        model instance.
        """
        self._test_name = "Test Receiver is not None Upon Instance Creation"
        try:
            self.assertIsNotNone(self._test_relationship.receiver)
        except AssertionError as error:
            logger.exception(f'Failed Test #3 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #3 - {self._test_name}')

    def test_status_is_SENT_by_default(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_status_is_SENT_by_default method checks to assure the
        status field of the Relationship model is SENT by default.
        """
        self._test_name = "Test Status is SENT by Default"
        try:
            self.assertEqual(
                self._test_relationship.status,
                Relationship.RequestOptions.SENT
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #4 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #4 - {self._test_name}')

    def test_updating_status_to_REJECTED(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_updating_status_to_REJECTED assures the status of a
        relationship can be properly transitioned to REJECTED.
        """
        self._test_name = "Test Updating Relationship status to REJECTED"
        try:
            self._test_relationship.update_status(
                status=Relationship.RequestOptions.REJECTED
            )

            self.assertEqual(
                self._test_relationship.status,
                Relationship.RequestOptions.REJECTED
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #5 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #5 - {self._test_name}')

    def test_updating_status_to_VIEWED(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_updating_status_to_VIEWED method assures the status
        of a relationship can be properly transitioned to VIEWED.
        """
        self._test_name = "Test Updating Relationship status to VIEWED"
        try:
            self._test_relationship.update_status(
                status=Relationship.RequestOptions.VIEWED
            )

            self.assertEqual(
                self._test_relationship.status,
                Relationship.RequestOptions.VIEWED
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #6 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #6 - {self._test_name}')

    def test_cancel_relationship(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The test_cancel_relationship method simulates the cancellation of
        a friendship request and asserts that the instance no longer exists.
        """
        self._test_name = "Test Cancel Relationship"
        try:
            sender  : settings.AUTH_USER_MODEL = self._test_relationship.sender
            receiver: settings.AUTH_USER_MODEL = self._test_relationship.receiver

            self._test_relationship.cancel()

            self.assertFalse(
                Relationship.get_relationship(
                    sender=sender,
                    receiver=receiver
                ).exists()
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #7 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #7 - {self._test_name}')

    def test_accepting_relationship(self) -> None:
        self._test_name = "Test Accepting Relationship"
        try:
            self._test_relationship.accept()

            sender_profile  : Profile = self._test_relationship.sender.profile
            receiver_profile: Profile = self._test_relationship.receiver.profile

            self.assertEqual(
                sender_profile.get_friends().first(),
                receiver_profile
            )

            self.assertEqual(
                receiver_profile.get_friends().first(),
                sender_profile
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #8 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #8 - {self._test_name}')

