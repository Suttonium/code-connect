from django.http               import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts          import render, redirect
from django.views              import View
from typing                    import Optional

from accounts.forms.user_registration_form import UserRegistrationForm


class UserRegistrationView(View):

    form : Optional[UserRegistrationForm] = None

    def _build_default_context(self, request: WSGIRequest) -> HttpResponse:
        self.form = UserRegistrationForm()

        return render(request, 'accounts/user_registration_template.html', {
                'form' : self.form
            }
        )

    def get(self, request: WSGIRequest, *args, **kwargs: dict) -> HttpResponse:
        return self._build_default_context(request=request)

    def post(self, request: WSGIRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        self.form = UserRegistrationForm(request.POST)

        if self.form.is_valid():
            self.form.save()
            return HttpResponse('Successfully Registered')
        else:
            return self._build_default_context(request=request)


