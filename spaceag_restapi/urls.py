from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi, views

schema_view = views.get_schema_view(
    openapi.Info(
        title='SpaceAG Challenge',
        default_version='v1',
        description='RestAPI Reto SpaceAG',
        contact=openapi.Contact(email='jdelacruzcr94@gmail.com'),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('field_workers/', include('app.urls')),
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
