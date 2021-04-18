from __future__ import annotations

import uuid

from django.conf              import settings
from django.db                import models
from django.utils.translation import ugettext_lazy as _

from accounts.managers.profile_manager import ProfileManager
from core.models.time_stamp            import TimeStamp


class Profile(TimeStamp):
    """
    The Profile class houses additional data about the user that is
    not needed during sign up, but rather added after the user has
    successfully joined the site.
    """

    class GenderOptions(models.TextChoices):
        """
        Houses the enumeration options used when a user designates
        their gender - if they so desire - on the frontend.
        Human-readble values will be inferred from the member names by
        replacing any underscores and using title-case automatically.
        """
        MALE              = 'M'
        FEMALE            = 'F'
        NON_BINARY        = 'N'
        PREFER_NOT_TO_SAY = 'X'


    uuid = models.UUIDField(
        _('UUID'), 
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    gender = models.CharField(
        _('Gender'),
        max_length=1,
        choices=GenderOptions.choices,
        default=GenderOptions.PREFER_NOT_TO_SAY
    )

    friends = models.ManyToManyField(
        'self',
        related_name='friends_list',
        blank=True
    )

    blocks = models.ManyToManyField(
        'self',
        related_name='blocked_users',
        blank=True
    )

    objects = ProfileManager()

    class Meta:
        """
        Profile.Meta class to define database-specific criterion.
        """
        db_table              = _('accounts-profile')
        verbose_name          = _('Profile')
        verbose_name_plural   = _('Profiles')
        order_with_respect_to =   'user'

    def __str__(self) -> str:
        """
        Parameters:
            None

        Returns:
            The desired string representation of the model for viewing
            in the database.

        The __str__ dunder method outputs the desired string representation
        of the Profile instance.
        """
        return f'Profile instance for {self.user.email}'

    @classmethod
    def create_profile(
        cls,
        *,
        user: settings.AUTH_USER_MODEL
    ) -> Profile:
        """
        Parameters:
            user -> the user who will own the new Profile instance

        Returns:
            An instance of the Profile class connected to the designated
            user.

        The new_profile class method handles the creation of a new Profile instance
        and keeps the creation logic inside the class itself.
        """
        return cls.objects.create_profile(
            user=user
        )

    def get_friends(self):
        """
        Paramters:
            None

        Returns:
            None

        The get_friends method returns the friends list of the current user.
        """
        return self.friends

    def add_friend(
        self,
        profile: Profile
    ) -> None:
        """
        Parameters:
            profile -> the profile being added to this instance's friends list.

        Returns:
            None

        The add_friend method handles finalizing a friendship request.
        """
        self.get_friends().add(profile)
        self.save()
