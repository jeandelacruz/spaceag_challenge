from django.urls import path
from .views import (
    WorkerListView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
)

urlpatterns = [
    path('', WorkerListView.as_view(), name='worker_list'),
    path('create', WorkerCreateView.as_view(), name='worker_create'),
    path(
        'update/<uuid:id>',
        WorkerUpdateView.as_view(),
        name='worker_update',
    ),
    path(
        'delete/<uuid:id>',
        WorkerDeleteView.as_view(),
        name='worker_delete',
    ),
]
