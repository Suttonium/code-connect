from __future__ import annotations

from django.db        import models
from django.db.models import Q


class UserQuerySet(models.QuerySet):

    def find(
        self,
        *,
        username: str,
        email: str
    ) -> UserQuerySet:
        return self.filter(
            Q(username=username) | Q(email=email)
        )
