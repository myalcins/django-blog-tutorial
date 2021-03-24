from django import forms
from django.contrib.auth.forms import UserChangeForm
from account.models import User


class ProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('avatar', 'email', 'username', 'first_name', 'last_name',)
