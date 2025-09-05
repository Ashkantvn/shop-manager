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


        if hasattr(user , "business_manager"): # Set business manager profile
            business_manager = user.business_manager
            business_manager_workers = user.business_manager.workers.all()
            business_manager_profile = {
                "manager": str(business_manager),
                "workers": business_manager_workers
            }
        
            return render(
                request, 
                'accounts/profile.html',
                context={
                    'profile':business_manager_profile,
                }
            )
        
        elif hasattr(user, "business_workers"):# Set business worker profile
            worker = user.business_workers
            working_times = user.business_workers.working_times.all()
            worker_profile = {
                "worker": str(worker),
                "working_times": working_times
            }
        
            return render(
                request, 
                'accounts/profile.html',
                context={
                    'profile':worker_profile,
                }
            )
        
        else:
            return render(
                request, 
                'accounts/profile.html',
                context={
                    'Error':"Something went wrong.",
                },
                status=HTTPStatus.BAD_REQUEST,
            )
        
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
        user = User.objects.filter(username=username).first()

        # Check user exist
        if not user:
            return render(
                request,
                'accounts/login.html',
                {
                    "error": 'User does not found.'
                },
                status= HTTPStatus.NOT_FOUND
            )
        
        # Check user password
        if user.check_password(password):
            login(request, user)
            return redirect('app-accounts:app-profile')
        else:
            return render(
                request, 
                'accounts/login.html', 
                {
                    'error': 'Password is incorrect.'
                },
                status=HTTPStatus.BAD_REQUEST
            )
    

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

        target_worker = models.BusinessWorker.objects.filter(
            user__user_slug=user_slug, 
            business_manager__user__username= user.username,    
        ).first()

        # Check if worker exist
        if not target_worker:
            return render(
                request,
                'accounts/login.html',
                {
                    "error": 'User does not found.'
                },
                status= HTTPStatus.NOT_FOUND
            )
        
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
    
    def get(self, request):
        """
        Handle the logout user.
        """
        logout(request)
        return redirect('app-accounts:login')