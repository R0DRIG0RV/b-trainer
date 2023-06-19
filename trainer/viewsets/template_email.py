from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from trainer.models.template_email import TemplateEmail
from trainer.serializers.template_email import TemplateEmailSerializer

class TemplateEmailViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TemplateEmailSerializer
    queryset = TemplateEmail.objects.all()