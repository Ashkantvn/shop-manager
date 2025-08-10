from django.views.generic import TemplateView

# Create your views here.
class AppProfileView(TemplateView):
    template_name = 'accounts/profile.html'
    