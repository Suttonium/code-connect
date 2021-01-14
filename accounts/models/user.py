import uuid

from django.contrib.auth.models import AbstractUser
from django.db                  import models
from django.utils.translation   import ugettext_lazy as _

from accounts.managers.user_manager import UserManager
from accounts.models.profile        import Profile


class User(AbstractUser):
    """
    The User class inherits from the built-in AbstractUser class to not only 
    give access to a custom user model, but to also override the built-in
    email field to mandate uniqueness.
    """

    uuid = models.UUIDField(
        _('UUID'), 
        primary_key=True, 
        default=uuid.uuid4,
        editable=False
    )

    email = models.EmailField(
        _('Email Address'),
        unique=True,
        help_text="The email address associated to this user."
    )

    is_banned = models.BooleanField(
        _('Banned Status'),
        default=False
    )

    objects = UserManager()

    class Meta:
        """
        User.Meta class to define database-specific criteria.
        """
        db_table            = _('accounts-users')
        verbose_name        = _('User')
        verbose_name_plural = _('Users')
        ordering            =  ['email']

    def __str__(self) -> str:
        """
        Parameters:
            None

        Returns:
            The desired string representation of the model for viewing
            in the database.
        """
        return self.email

    def save(self, *args, **kwargs) -> None:
        """
        Parameters:
            *args    -> multiple arguments passed by the django internals
            **kwargs -> keyword arguments passed by the django internals

        Returns:
            None
        """
        super().save(*args, **kwargs)
        
        if not hasattr(self, 'profile'):
            Profile.objects.create(user=self)
