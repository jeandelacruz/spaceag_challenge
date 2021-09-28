from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from .serializers import WorkerSerializer
from .models import Worker

# Create your views here.
class WorkerListView(GenericAPIView, ListModelMixin):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class WorkerCreateView(GenericAPIView, CreateModelMixin):
    serializer_class = WorkerSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class WorkerUpdateView(GenericAPIView, UpdateModelMixin):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class WorkerDeleteView(GenericAPIView, DestroyModelMixin):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
