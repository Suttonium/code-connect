from django.core.handlers.wsgi import WSGIRequest
from django.http               import HttpResponse
from django.shortcuts          import get_object_or_404, render
from django.views              import View

from accounts.models.profile import Profile
from accounts.models.user    import User


class ProfileDetailView(View):

    def get(self, request: WSGIRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        user   : User    = User.objects.get(username=kwargs['username'])
        profile: Profile = get_object_or_404(Profile, user=user)

        if profile:
            return render(request, 'accounts/profile_detail_template.html', {
                    'profile': profile,
                    'user'   : user
                }
            )
        else:
            ...

ProfileDetailView = ProfileDetailView.as_view()

