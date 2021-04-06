import logging
import uuid

from django.conf              import settings
from django.db                import models
from django.utils.translation import ugettext_lazy as _

from accounts.exception     import AccountsException
from core.models.time_stamp import TimeStamp

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

    def __str__(self) -> str:
        """
        Parameters:
            None

        Returns:
            The desired string representation of the model for viewing
            in the database.
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

    def save(self, *args: tuple, **kwargs: dict):
        logger.info('Started Relationship.save')

        if self.sender == self.receiver:
            logger.warning('The sender and receiver of this relationship are equal')
            raise AccountsException

        super().save(*args, **kwargs)

        logger.info('Completed Relationship.save')

    @classmethod
    def new_relationship(
        cls,
        *, 
        sender: settings.AUTH_USER_MODEL,
        receiver: settings.AUTH_USER_MODEL
    ):
        return cls.objects.create(
            sender=sender,
            receiver=receiver
        )
    
    def accept(self) -> None:
        self.sender.friends.add(self.receiver)
        self.receiver.friends.add(self.sender)

        # remove the request from the database because it has been accepted
        self.delete()

    def reject(self) -> None:
        self.status = RequestOptions.REJECTED
        self.save()

    def cancel(self) -> None:
        self.delete()
