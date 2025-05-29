from django.shortcuts import redirect


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
            and not request.path.startswith('/accounts/login/') 
            and not request.path.startswith('/admin/login/')
            and not request.path.startswith('/api/v1/accounts/login/')      
        ):
            return redirect('/admin/login/')  # Redirect to the login page if not authenticated
        response = self.get_response(request)
        return response