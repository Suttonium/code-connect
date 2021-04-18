from __future__ import annotations

from django.conf import settings
from django.db   import models


class RelationshipQuerySet(models.QuerySet):

    def find(
        self,
        sender: settings.AUTH_USER_MODEL,
        receiver: settings.AUTH_USER_MODEL
    ) -> RelationshipQuerySet:
        return self.filter(
            sender=sender,
            receiver=receiver
        )
