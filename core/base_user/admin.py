"""
User admininistration compatable AbstractEmailUser
"""

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


class UserAdmin(DjangoUserAdmin):

    """
    user admin class compatable with AbstractEmailUser
    """
    list_display = ('email', 'first_name', 'last_name', 'is_staff', )
    ordering = ('email', )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Information', {'fields': ('first_name', 'last_name', )}),
        ('Status/Access', {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')})
    )

    add_fieldsets = (
        (None, {'classes': ('wide', ), 'fields': (
            'email', 'first_name', 'last_name', 'password',)}),
    )
