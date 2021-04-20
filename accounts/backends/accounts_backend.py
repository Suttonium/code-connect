import logging

from django.contrib.auth.backends import ModelBackend
from django.core.handlers.wsgi    import WSGIRequest
from django.db.models             import Q
from typing                       import Optional

from accounts.models.user             import User
from accounts.querysets.user_queryset import UserQuerySet


logger = logging.getLogger('accounts')

class AccountsBackend(ModelBackend):
    """
    The EmailBackend class handles authentication for a user when they use their
    email to log in.
    """

    user: Optional[User] = None
    
    def authenticate(
        self,
        request: WSGIRequest,
        **kwargs: dict
    ) -> User:
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

        query: UserQuerySet = User.get_user(
            username=username,
            email=email
        )

        # if the QuerySet returned a successful find
        if query.exists():
            self.user = query.first()
            if not self.user.authenticate(password=password)
                self.user = None
        else:
            self.user = None

        logger.info('Completed AccountsBackend.authenticate method')
        return self.user

        
