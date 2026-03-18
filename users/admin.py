from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role


admin.site.register(Role)


class CustomUserAdmin(UserAdmin):
    model = User
    
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Roles', {'fields': ('roles',)}),
    )
    
    list_display = ['email', 'username', 'is_staff', 'is_active']

admin.site.register(User, CustomUserAdmin)