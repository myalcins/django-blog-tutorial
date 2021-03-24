from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from account.forms import ProfileForm


@login_required(login_url='/')
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
    form = ProfileForm(instance=request.user)
    return render(request, 'pages/edit-profile.html', context={
        "form": form
    })
