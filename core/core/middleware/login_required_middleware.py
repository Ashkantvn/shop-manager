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
        # Allow access static files
        if request.path.startswith('/static/') or request.path.startswith('/media/'):
            return self.get_response(request)
        
        # Skip force authentication of api and django template login page
        if request.path.startswith('/api/') :
            return self.get_response(request)

        if (
            not request.user.is_authenticated 
            and not request.path.startswith('/accounts/login/')
            and not request.path.startswith('/admin/login/')
        ):
            response = HttpResponseRedirect('/accounts/login/') 
            response.status_code = 401
            return response
        response = self.get_response(request)
        return response