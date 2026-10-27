"""
URL configuration for techstore project.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración personalizada de OpenAPI / Swagger para TechStore API
schema_view = get_schema_view(
    openapi.Info(
        title="TechStore API",
        default_version='v1',
        description=(
            "Documentación interactiva de la API de TechStore.\n\n"
            "Incluye autenticación mediante JWT (JSON Web Tokens), gestión completa de usuarios (CRUD), "
            "endpoint de datos de perfil (/auth/me/), y catálogo de productos (Unidad 1)."
        ),
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contacto@techstore.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),

    # Endpoints de la API REST (v1)
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('products.urls')),

    # Documentación Swagger / OpenAPI
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
