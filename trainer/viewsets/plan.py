from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from trainer.models.plan import Plan
from trainer.serializers.plan import PlanSerializer

class PlanViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()