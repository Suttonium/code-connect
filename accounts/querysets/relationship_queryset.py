from __future__ import annotations

from django.conf import settings
from django.db   import models


class RelationshipQuerySet(models.QuerySet):
    """
    The RelationshipQuerySet class is meant to handle
    table-wide database queries by using the Django
    built-in query functionality.
    """

    def find(
        self,
        *,
        sender: settings.AUTH_USER_MODEL,
        receiver: settings.AUTH_USER_MODEL
    ) -> RelationshipQuerySet:
        """
        Parameters:
            sender   -> The user who initiated the friend request
            receiver -> The user who received the friend request

        Returns:
            A chainable QuerySet representing the filtered Relationship
            instance

        The find method is designed to return a QuerySet rather than a
        Relationship instance so the .exists() method can be used upon
        its return.
        """
        return self.filter(
            sender=sender,
            receiver=receiver
        )
