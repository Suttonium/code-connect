import logging
import uuid

from django.contrib.auth.models import AbstractUser
from django.db                  import models
from django.utils.translation   import ugettext_lazy as _

from accounts.managers.user_manager import UserManager
from accounts.models.profile        import Profile

logger = logging.getLogger('accounts')


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

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

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
        logger.info('Started User.save')

        super().save(*args, **kwargs)
        
        if not hasattr(self, 'profile'):
            Profile.new_profile(user=self)

        logger.info('Completed User.save')

    @classmethod
    def new_user(cls, *, email: str, username: str) -> models.base.ModelBase:
        """
        Parameters:
            email    -> desired email for user creation
            username -> desired username for user creation

        Returns:
            An instance of this class create through an ORM method call
        """
        return cls.objects.create(
            email=email,
            username=username,
        )

    def authenticate(self, *, password: str) -> models.base.ModelBase:
        return self.check_password(password) and not self.is_banned and self.is_active
