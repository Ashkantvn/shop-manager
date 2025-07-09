from django.shortcuts import redirect
from django.http import HttpResponseRedirect


class LoginRequiredMiddleware:
    """
    Middleware to ensure that the user is authenticated before accessing certain views.
    If the user is not authenticated, they are redirected to the login page.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            not request.user.is_authenticated 
            and not request.path.startswith('/api/v1/accounts/login/') 
            and not request.path.startswith('/admin/login/')
        ):
            response = HttpResponseRedirect('/admin/login/')
            response.status_code = 401
            return response
        response = self.get_response(request)
        return response