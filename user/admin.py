from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class UserAdmin(DefaultUserAdmin):
    """
    Custom UserAdmin model for User model.

    This class is used to register User model in admin interface and
    customize the interface for the model.
    """
    model = User
    ordering = ['email']
    list_display = ('email', 'first_name', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone', 'avatar', 'gender', 'birthday_date', 'region')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'phone', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ('user_permissions',)
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, UserAdmin)
