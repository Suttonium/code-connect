from django.contrib.auth.backends import ModelBackend
from django.core.handlers.wsgi    import WSGIRequest
from django.db.models             import Q
from typing                       import Optional

from accounts.models.user import User


class AccountsBackend(UserAuthMixin, ModelBackend):
    """
    The EmailBackend class handles authentication for a user when they use their
    email to log in.
    """
    
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
        try:
            user: User = User.objects.get(Q(username=username) | Q(email=username))
            if user.authenticate(password=password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None
