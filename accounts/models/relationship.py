from __future__ import annotations

import logging
import uuid

from django.conf              import settings
from django.db                import models
from django.db.models.query   import QuerySet
from django.utils.translation import ugettext_lazy as _

from accounts.exception                       import AccountsException
from accounts.managers.relationship_manager   import RelationshipManager
from accounts.querysets.relationship_queryset import RelationshipQuerySet
from core.models.time_stamp                   import TimeStamp

logger = logging.getLogger('accounts')


class Relationship(TimeStamp):
    """
    The Relationship class represents the current status of a 
    friend request between two Profile instances.
    """

    class RequestOptions(models.TextChoices):
        """
        The RequestOptions enumeration class is used to store
        the request status of an outgoing friend request.
        Human-readable values will be inferred from the member names
        by replacing any underscores and using title-case automatically.
        There is no option for accepted because the relationship instance
        will be removed from the database when it is accepted.
        """
        SENT     = 'S'
        REJECTED = 'R'
        VIEWED   = 'V'


    uuid = models.UUIDField(
        _('UUID'),
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sender'
    )

    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='receiver'
    )

    status = models.CharField(
        _('Status'),
        max_length=1,
        choices=RequestOptions.choices,
        default=RequestOptions.SENT
    )

    objects = RelationshipManager()

    def __str__(self) -> str:
        """
        Parameters:
            None

        Returns:
            The desired string representation of the model for viewing
            in the database.

        The __str__ dunder method outputs the desired string representation
        of the Relationship instance.
        """
        return f'Friend Request between {self.sender} and {self.receiver}'
        

    class Meta:
        """
        Relationship.Meta class to define database-specific criterion.
        """
        db_table            = _('accounts-relationship')
        ordering            =  ['created']
        unique_together     =  ('sender', 'receiver')
        verbose_name        = _('Relationship')
        verbose_name_plural = _('Relationships')

    def save(
        self,
        *args: tuple,
        **kwargs: dict
    ) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The save method saves the current relationship to the database and
        also assures that the sender and receiver of the instance cannot be
        the same user.
        """
        logger.info('Started Relationship.save')

        if self.sender == self.receiver:
            logger.warning('The sender and receiver of this relationship are equal')
            raise AccountsException

        super().save(*args, **kwargs)

        logger.info('Completed Relationship.save')

    @classmethod
    def create_relationship(
        cls,
        *, 
        sender: settings.AUTH_USER_MODEL,
        receiver: settings.AUTH_USER_MODEL
    ) -> Relationship:
        """
        Parameters:
            sender   -> The user initiating the friend request
            receiver -> The user receiving the friend request

        Returns:
            A new Relationship instance representing the friend
            request between the sender and the receiver.

        The new_relationship class method is used to keep class-level
        instance creation inside the class itself.
        """
        return cls.objects.create(
            sender=sender,
            receiver=receiver
        )

    @classmethod
    def get_relationship(
        cls,
        *,
        sender: settings.AUTH_USER_MODEL,
        receiver: settings.AUTH_USER_MODEL
    ) -> RelationshipQuerySet:
        """
        The get_relationship class methods performs a filter of the
        Relationship instances by using the unique combination of
        sender and receiver dictated in the static Meta class.
        """
        return cls.objects.find(
            sender=sender,
            receiver=receiver
        )
    
    def accept(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The accept method is used to finalize a friend request between
        two users and it also removes the request from the database after
        acceptance.
        """
        self.sender.profile.add_friend(profile=self.receiver.profile)
        self.receiver.profile.add_friend(profile=self.sender.profile)

        # remove the request from the database because it has been accepted
        self.delete()

    def reject(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The reject method is used to showcase that a friend request
        was rejected by a user.
        """
        self.status = self.RequestOptions.REJECTED

    def mark_as_viewed(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The marked_as_viewed method designates that a friend request
        was viewed by the recipient.
        """
        self.status = self.RequestOptions.VIEWED

    def cancel(self) -> None:
        """
        Parameters:
            None

        Returns:
            None

        The cancel method ends the friend request by removing it from the database.
        """
        self.delete()

    def update_status(
        self,
        *,
        status: RequestOptions
    ) -> None:
        """
        Parameters:
            status -> the desired status of the friend request

        Returns:
            None

        The update_status method takes in a RequestOptions enumerated
        value and updates the relationship's status accordingly.
        """
        logger.info('Started Relationship.update_status')

        if status == self.RequestOptions.REJECTED:
            self.reject()
        elif status == self.RequestOptions.VIEWED:
            self.mark_as_viewed()
        elif status == self.RequestOptions.SENT:
            # this should not be used because SENT
            # is the default status
            pass

        self.save()

        logger.info('Completed Relationship.update_status')

