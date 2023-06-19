from rest_framework.serializers import ModelSerializer
from trainer.models.plan import Plan


class PlanSerializer(ModelSerializer):

    class Meta:
        model = Plan
        fields = (
            'id',
            'user',
            'name',
            'description',
            'price',
            'duration',
            'discount',
            'price_discount',
            'created_at'
        )

    def to_representation(self, instance: Plan) -> dict:
        from trainer.serializers.user import UserSerializer

        data = super(PlanSerializer, self).to_representation(instance)

        data.update({
            'user': UserSerializer(instance=instance.user).data,
        })

        return data
