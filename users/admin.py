from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Configuración del modelo de Usuario en el panel de Administración de Django.
    Muestra el campo extra 'telefono' en los formularios y listas.
    """
    list_display = ('id', 'email', 'username', 'first_name', 'last_name', 'telefono', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', 'username', 'first_name', 'last_name', 'telefono')
    ordering = ('id',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('username', 'first_name', 'last_name', 'telefono')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'first_name', 'last_name', 'telefono', 'is_staff', 'is_superuser'),
        }),
    )
