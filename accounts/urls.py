from django.contrib.auth import views as auth_views
from django.urls         import path

from accounts.views.user_login_view        import UserLoginView
from accounts.views.user_registration_view import UserRegistrationView


urlpatterns = [
    path('login/', UserLoginView, name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration')
]
