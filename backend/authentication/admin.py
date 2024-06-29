from django.contrib import admin
from .models import CustomUser, UserProfile
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email','username','is_active','is_staff','is_superuser','is_verified','date_joined','last_login']
    search_fields = ['email','username']
    list_filter = ['is_active','is_staff','is_superuser','is_verified']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_verified')}),
        ('Important dates', {'fields': ('date_joined', 'last_login')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    ordering = ['email']
    filter_horizontal = ()
@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ['user','first_name','last_name','phone']
    search_fields = ['user','first_name','last_name','phone']
