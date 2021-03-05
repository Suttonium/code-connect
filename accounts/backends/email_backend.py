from django.contrib.auth.backends import ModelBackend
from django.core.handlers.wsgi    import WSGIRequest
from typing                       import Optional

from accounts.models.user import User


class EmailBackend(ModelBackend):
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

        # email will be treated as the username in this case
        email   : str = kwargs['username'] 
        password: str = kwargs['password']

        try:
            self.user = User.objects.get(email=email)
            if self.user.check_password(password):
                if not self.user.is_banned and self.user.is_active:
                    return self.user
        except User.DoesNotExist:
            ...
