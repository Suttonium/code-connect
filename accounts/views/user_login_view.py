from django.contrib.auth       import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http               import HttpResponse
from django.shortcuts          import render
from django.views              import View
from typing                    import Optional

from accounts.models.user import User


class UserLoginView(View):
    form: Optional[AuthenticationForm] = None

    def get(self, request, *args: tuple, **kwargs: dict) -> HttpResponse:
        self.form = AuthenticationForm()
        return render(request, 'accounts/user_login_template.html', {
                'form': self.form
            }
        )

    def post(self, request, *args: tuple, **kwargs: dict) -> HttpResponse:
        self.form = AuthenticationForm(request.POST)

        username: str = request.POST['username']
        password: str = request.POST['password']
        
        user: User = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponse(f'Logged in {user}')
            else:
                ...
        else:
            return HttpResponse('User is NONE')

UserLoginView = UserLoginView.as_view()
