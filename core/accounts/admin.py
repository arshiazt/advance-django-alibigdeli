from django.contrib import admin
from .models import User,Profile
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):

    models = User
    list_display = ('email','is_active','is_staff','is_superuser','is_verified')
    list_filter = ('email','is_active','is_staff','is_superuser','is_verified')
    search_fields = ('email',)
    ordering = ('-created_date',)
    fieldsets = (
        ('Authentication',{
            'fields':(
                'email','password'
            )
        }),
        ('Permissions',{
            'fields':(
                'is_active','is_staff','is_superuser','is_verified'
            )
        }),
        ('Group Permissions',{
            'fields':(
                'groups','user_permissions'
            )
        }),
        ('Importants Dates',{
            'fields':(
                'last_login',
            )
        })
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2','is_active','is_staff','is_superuser','is_verified')
        }),
    )


admin.site.register(User,CustomUserAdmin)
admin.site.register(Profile)