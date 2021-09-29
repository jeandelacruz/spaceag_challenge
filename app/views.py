from rest_framework.viewsets import ModelViewSet
from .serializers import WorkerSerializer
from .models import Worker

# Create your views here.
class WorkerViewSet(ModelViewSet):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
    lookup_field = 'id'
