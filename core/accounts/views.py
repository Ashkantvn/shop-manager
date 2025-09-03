from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, login, logout
from accounts import models
from http import HTTPStatus
from datetime import datetime

User = get_user_model()

# Create your views here.
class AppProfileView(View):

    def get(self, request):

        user = request.user
        profile = user

        if hasattr(user , "business_manager"):
            business_manager = user.business_manager
            business_manager_workers = user.business_manager.workers.all()
            profile = {
                "business_manager": business_manager,
                "business_manager_workers": business_manager_workers
            }
        elif hasattr(user, "business_workers"):
            profile = user.business_workers


        return render(request, 'accounts/profile.html',context={'profile':profile})
    

# Login view for the app
class AppLoginView(View):
    
    def get(self, request):
        """
        Render the login page for the app.
        """
        return render(request, 'accounts/login.html')
    
    def post(self, request):
        """
        Handle the login form submission for the app.
        """
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = get_object_or_404(User, username=username)
        if user.check_password(password):
            login(request, user)
            return redirect('app-accounts:app-profile')
        else:
            return render(request, 'accounts/login.html', {'error': 'Password is incorrect'})
    

# User update view
class AppUserUpdateView(View):

    def get(self,request,user_slug):
        """
        Render user update page
        """    
        return render(request, 'accounts/update.html')
    
    def post(self, request, user_slug):
        """
        Set working time for workers
        """
        user = request.user

        target_worker = get_object_or_404(models.BusinessWorker,user__user_slug=user_slug , business_manager__user__username=user.username)
        
        # Validate post data
        start_time_str = request.POST.get('start_time')
        end_time_str = request.POST.get('end_time')

        start_time = datetime.strptime(start_time_str, "%H:%M").time()
        end_time = datetime.strptime(end_time_str, "%H:%M").time()

        if start_time > end_time:
            return render(
                request,
                'accounts/update.html',
                context={
                    "error": "Start time cannot be after end time"
                },
                status= HTTPStatus.BAD_REQUEST
            )
        else:
            models.WorkingTime.objects.create(
                start_time = start_time_str,
                end_time = end_time_str,
                business_worker = target_worker
            )
            return render(
                request,
                'accounts/update.html',
                context={ "data":"Working time created"},
                status= HTTPStatus.CREATED
            )

# Logout view for the app
class AppLogoutView(View):
    pass