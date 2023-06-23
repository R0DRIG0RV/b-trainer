from rest_framework.serializers import ModelSerializer
from trainer.models.client import Client


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = (
            'id',
            'user',
            'plan',
            'dni',
            'firstname',
            'lastname',
            'email',
            'created_at'
        )

    def to_representation(self, instance: Client) -> dict:
        from trainer.serializers.user import UserSerializer
        from trainer.serializers.plan import PlanSerializer

        data = super(ClientSerializer, self).to_representation(instance)

        data.update({
            'user': UserSerializer(instance=instance.user).data,
            'plan': PlanSerializer(instance=instance.plan).data,
        })

        return data
    
    def create(self, validated_data: dict) -> dict:
        validated_data['user'] = self.context['request'].user
        return super(ClientSerializer, self).create(validated_data)
