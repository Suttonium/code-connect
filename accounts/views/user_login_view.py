from django.contrib.auth       import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.handlers.wsgi import WSGIRequest
from django.http               import HttpResponse
from django.shortcuts          import render, redirect
from django.views              import View
from typing                    import Optional

from accounts.models.user import User


class UserLoginView(View):
    form: Optional[AuthenticationForm] = None

    def _build_default_context(self, request: WSGIRequest) -> HttpResponse:
        self.form = AuthenticationForm()

        return render(request, 'accounts/user_login_template.html', {
                'form': self.form
            }
        )

    def get(self, request: WSGIRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        return self._build_default_context(request=request)

    def post(self, request: WSGIRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        self.form = AuthenticationForm(request.POST)

        username: str = request.POST['username']
        password: str = request.POST['password']
        
        user: User = authenticate(username=username, password=password)

        if user and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            return self._build_default_context(request=request)

UserLoginView = UserLoginView.as_view()
