from django.contrib import admin
from django.urls import path, include
from .openapi import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/field_workers/', include('app.urls')),
    path(
        '',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'api/api.json/',
        schema_view.without_ui(cache_timeout=0),
        name='schema-swagger-w-ui',
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='shecma-redoc',
    ),
]
