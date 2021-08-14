from django.contrib             import admin
from django.contrib.auth.models import Group

from accounts.admin.user_admin  import UserAdmin
from accounts.models.profile    import Profile
from accounts.models.user       import User


# register all admin classes here
admin.site.register(Profile)
admin.site.register(User, UserAdmin)

# unregister any admin classes here if needed
admin.site.unregister(Group)
