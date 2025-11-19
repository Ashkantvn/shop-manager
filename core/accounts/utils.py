from django.shortcuts import render

def render_login_success(request):
    return render(
        request,
        'accounts/login.html',
        {
            "message": "Login successful!"
        }
    )