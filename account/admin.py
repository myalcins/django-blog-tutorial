from account.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Upload Avatar', {
            'fields': ['avatar']
        }),
    )
