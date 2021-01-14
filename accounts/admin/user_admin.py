from django.contrib             import admin
from django.contrib.auth.models import Group

from accounts.models.user import User


class UserAdmin(admin.ModelAdmin):
    """
    The UserAdmin class customizes the admin pages
    associated to the User model.
    """
    
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
    )

    list_filter = (
        'is_banned',
        'date_joined',
        'is_staff'
    )

    exclude = (
        'groups',
        'user_permissions',
    )

