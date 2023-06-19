from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from trainer.models.client import Client
from trainer.serializers.client import ClientSerializer

class ClientViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()