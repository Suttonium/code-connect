import logging

from django.contrib.auth.backends import ModelBackend
from django.core.handlers.wsgi    import WSGIRequest
from django.db.models             import Q
from typing                       import Optional

from accounts.models.user import User


logger = logging.getLogger('accounts')

class AccountsBackend(ModelBackend):
    """
    The EmailBackend class handles authentication for a user when they use their
    email to log in.
    """

    user: Optional[User] = None
    
    def authenticate(self, request: WSGIRequest, **kwargs: dict) -> User:
        """
        Parameters:
            request  -> the WSGIRequest object sent when 'submit'
                        is hit on the frontend

            **kwargs -> the dictionary of inputs gathered from the form

        Returns:
            A user object if the user was authenticated properly, otherwise an error
            will be raised
        """
        logger.info('Started AccountsBackend.authenticate method')

        username: str = kwargs['username']
        password: str = kwargs['password']

        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if not user.authenticate(password=password):
                user = None
        except User.DoesNotExist:
            user = None

        logger.info('Completed AccountsBackend.authenticate method')
        return user

        
