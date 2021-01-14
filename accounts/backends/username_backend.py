from django.contrib.auth.backends import ModelBackend
from django.core.handlers.wsgi    import WSGIRequest

from accounts.models.user import User


class UsernameBackend(ModelBackend):
    """
    The UsernameBackend class handles authentication
    for a user when the use their username to log in.
    """

    def authenticate(self, request: WSGIRequest, **kwargs: dict) -> User:
        """
        Parameters:
            request  -> the WSGIRequest object sent when 'submit'
                        is hit on the frontend

            **kwargs -> the dictionary of inputs gathered from
                        the form

        Returns:
            A user object if the user was authenticated properly,
            otherwise an error will be raised
        """
        username: str = kwargs['username']
        password: str = kwargs['password']

        try:
            user: User = User.objects.get(username=username)
            if user.check_password(password):
                if not user.is_banned:
                    return user
        except User.DoesNotExist:
            ...
