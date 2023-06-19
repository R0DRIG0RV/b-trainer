from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from trainer.models.client_document import ClientDocument
from trainer.serializers.client_document import ClientDocumentSerializer

class ClientDocumentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ClientDocumentSerializer
    queryset = ClientDocument.objects.all()