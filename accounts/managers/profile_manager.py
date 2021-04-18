from django.conf import settings
from django.db   import models

from accounts.querysets.profile_queryset import ProfileQuerySet


class ProfileManager(models.Manager):

    def create_profile(
        self,
        *,
        user: settings.AUTH_USER_MODEL
    ):
        return self.model(
            user=user
        )

    def get_queryset(self) -> ProfileQuerySet:
        return ProfileQuerySet(self.model, using=self._db)
