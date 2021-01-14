from django.urls import path

from accounts.views.user_registration_view import UserRegistrationView


urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration')
]
