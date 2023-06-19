from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from trainer.models.note import Note
from trainer.serializers.note import NoteSerializer

class NoteViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = NoteSerializer
    queryset = Note.objects.all()