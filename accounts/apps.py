from django.apps              import AppConfig
from django.conf              import settings
from django.db.models.signals import post_save



class AccountsConfig(AppConfig):
    name = 'accounts'

