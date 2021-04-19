from django.conf import settings
from django.db   import models

from accounts.querysets.relationship_queryset import RelationshipQuerySet


class RelationshipManager(models.Manager):
    """
    The RelationshipManager class handles table-wide
    database queries for the Relationship class.
    """

    def create_relationship(
        self,
        *,
        sender: settings.AUTH_USER_MODEL,
        receiver: settings.AUTH_USER_MODEL
    ):
        relationship = self.model(
            sender=sender,
            receiver=receiver
        )
        relationship.save()

        return relationship

    def get_queryset(self) -> RelationshipQuerySet:
        return RelationshipQuerySet(self.model, using=self._db)

    def find(
        self,
        *,
        sender: settings.AUTH_USER_MODEL,
        receiver: settings.AUTH_USER_MODEL
    ) -> RelationshipQuerySet:
        return self.get_queryset().find(
            sender=sender,
            receiver=receiver
        )

