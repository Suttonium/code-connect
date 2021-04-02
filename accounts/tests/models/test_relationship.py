import logging

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
        try:
            self.assertIsNotNone(self._test_relationship.uuid)
        except AssertionError as error:
            logger.exception('Failed Test #1 - Test uuid is not none')
            self.fail()
        else:
            logger.info('Completed Test #1 - Test uuid is not none')
