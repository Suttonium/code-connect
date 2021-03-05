from django.db import models

from accounts.querysets.profile_queryset import ProfileQuerySet


class ProfileManager(models.Manager):

    def get_queryset(self) -> ProfileQuerySet:
        return ProfileQuerySet(self.model, using=self._db)
