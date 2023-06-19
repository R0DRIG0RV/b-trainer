from rest_framework.serializers import ModelSerializer
from trainer.models.user import User

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email'
        )