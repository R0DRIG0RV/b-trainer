from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from trainer.models.document import Document
from trainer.serializers.document import DocumentSerializer

class DocumentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()