from django.contrib.auth.models import BaseUserManager

from accounts.querysets.user_queryset import UserQuerySet


class UserManager(BaseUserManager):
    """
    The UserManager class handles all of the table-wide
    queries and actions on the User model. Each function call
    within this object will call a related helper function
    implemented in the UserQuerySet class.
    """
    
    def get_queryset(self) -> UserQuerySet:
        """
        Parameters:
            None

        Returns:
            A UserQuerySet object used for any subsequent queries.
        """
        return UserQuerySet(self.model, using=self._db)
