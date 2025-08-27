from django.views import View
from django.shortcuts import render
from django.contrib.auth import get_user_model
from accounts.models import BusinessWorker

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
    