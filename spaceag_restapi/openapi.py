from drf_yasg import openapi, views
from drf_yasg.generators import OpenAPISchemaGenerator


class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, *args, **kwargs):
        schema = super().get_schema(*args, **kwargs)
        schema.basePath = '/v1'
        return schema


schema_view = views.get_schema_view(
    openapi.Info(
        title='SpaceAG Challenge',
        default_version='v1',
        description='RestAPI Reto SpaceAG',
        contact=openapi.Contact(email='jdelacruzcr94@gmail.com'),
    ),
    public=True,
    generator_class=CustomOpenAPISchemaGenerator,
)
