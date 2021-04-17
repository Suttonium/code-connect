from django.db import models

from accounts.querysets import RelationshipQuerySet


class RelationshipManager(models.Manager):
    """
    The RelationshipManager class handles table-wide
    database queries for the Relationship class.
    """

    def get_queryset(self) -> RelationshipQuerySet:
        return RelationshipQuerySet(self.model, using=self._db)

