from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def log_out(request):
    logout(request)
    return redirect('homepage')