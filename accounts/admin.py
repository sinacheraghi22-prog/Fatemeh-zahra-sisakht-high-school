from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'get_full_name', 'role', 'email', 'is_active')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'national_code')
    
    fieldsets = UserAdmin.fieldsets + (
        ('اطلاعات تکمیلی', {
            'fields': ('role', 'phone', 'national_code', 'avatar')
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('اطلاعات تکمیلی', {
            'fields': ('role', 'phone', 'national_code'),
        }),
    )
