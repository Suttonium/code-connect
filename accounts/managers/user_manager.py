from django.contrib.auth.models import BaseUserManager

from accounts.querysets.user_queryset import UserQuerySet


class UserManager(BaseUserManager):
    """
    The UserManager class handles all of the table-wide
    queries and actions on the User model. Each function call
    within this object will call a related helper function
    implemented in the UserQuerySet class.
    """
    
    def create_user(
        self,
        *,
        username: str,
        email: str,
        password: str,
        **extra_fields: dict
    ):
        """
        Parameters:
            username       -> the username used during user creation
            email          -> the email used during user creation
            password       -> the password used during user creation
            **extra_fields -> additional fields to be added by default

        Returns:
            A user object that has been added to the database
        """
        if not email:
            raise ValueError('An email address must be supplied')

        if not username:
            raise ValuError('A username must be supplied')

        user = self.model(
            email=self.normalize_email(email),
            username=username, 
            **extra_fields
        )
        user.set_password(password)

        user.save()
        return user

    def create_superuser(
        self,
        *,
        username: str,
        email: str,
        password: str,
            **extra_fields: dict
    ):
        """
        Parameters:
            username       -> the username used during user creation
            email          -> the email used during user creation
            password       -> the password used during user creation
            **extra_fields -> additional fields to be added by default

        Returns:
            A superuser object for admin access to the database
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
