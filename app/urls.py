from django.urls import path
from .views import WorkerViewSet

urlpatterns = [
    path(
        '',
        WorkerViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='list_create',
    ),
    path(
        '<uuid:id>',
        WorkerViewSet.as_view({'patch': 'update', 'delete': 'destroy'}),
        name='update_destroy',
    ),
]
