from django.urls import path

from accounts.views.profile_detail_view    import ProfileDetailView
from accounts.views.user_login_view        import UserLoginView
from accounts.views.user_registration_view import UserRegistrationView


urlpatterns = [
    path('login/', UserLoginView, name='login'),
    path('registration/', UserRegistrationView, name='registration'),
    path('<str:username>/', ProfileDetailView, name='profile_detail')
]
