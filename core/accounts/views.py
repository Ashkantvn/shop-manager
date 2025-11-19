from django.shortcuts import render, redirect
from django.views import View
from http import HTTPStatus as status
from django.contrib.auth import authenticate, login, logout
from accounts.utils import render_login_success
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')
    
    def post(self, request):
        username = request.POST.get('username',"")
        password = request.POST.get('password',"")
        # If user is already authenticated, render login page with success message
        if request.user.is_authenticated:
            return render_login_success(request)
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render_login_success(request)
        else:
            return render(
                request,
                'accounts/login.html',
                {
                    'error': 'Authentication not provided or user not found.'
                },
                status=status.UNAUTHORIZED
            )

            

class LogoutView(LoginRequiredMixin,View):
    def post(self, request):
        logout(request)
        return redirect('accounts:login')