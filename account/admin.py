from account.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Upload Avatar', {
            'fields': ['avatar']
        }),
    )

admin.site.register(User, UserAdmin)