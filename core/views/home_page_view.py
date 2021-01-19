from django.core.handlers.wsgi import WSGIRequest
from django.http               import HttpResponse
from django.shortcuts          import render
from django.views              import View


class HomePageView(View):

    def get(self, request: WSGIRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        return render(request, 'home_page_template.html', {
                'user': request.user
            }
        )

HomePageView = HomePageView.as_view()
