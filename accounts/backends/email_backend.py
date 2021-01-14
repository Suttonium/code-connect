from django.contrib.auth.backends import ModelBackend
from django.core.handlers.wsgi    import WSGIRequest

from accounts.models.user import User


class EmailBackend(ModelBackend):
    
    def authenticate(self, request: WSGIRequest, **kwargs: dict) -> User:

        # email will be treated as the username in this case
        email   : str = kwargs['username'] 
        password: str = kwargs['password']

        try:
            user: User = User.objects.get(email=email)
            if user.check_password(password) and not user.is_banned:
                return user
        except User.DoesNotExist:
            ...
