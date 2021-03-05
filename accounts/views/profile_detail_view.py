import logging

from django.core.handlers.wsgi import WSGIRequest
from django.http               import HttpResponse
from django.shortcuts          import get_object_or_404, render
from django.views              import View
from typing                    import Optional

from accounts.models.profile import Profile
from accounts.models.user    import User

logger = logging.getLogger('accounts')

class ProfileDetailView(View):

    user   : Optional[User]    = None
    profile: Optional[Profile] = None

    def get(self, request: WSGIRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        logger.info('Started ProfileDetailView.get method')

        user    = request.user
        profile = get_object_or_404(Profile, user=user)

        if profile:
            return render(request, 'accounts/profile_detail_template.html', {
                    'profile': profile,
                    'user'   : user
                }
            )
        else:
            ...

        logger.info('Completed ProfileDetailView.get method')

ProfileDetailView = ProfileDetailView.as_view()

