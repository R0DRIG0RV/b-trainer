from rest_framework.serializers import ModelSerializer
from trainer.models.template_email import TemplateEmail


class TemplateEmailSerializer(ModelSerializer):

    class Meta:
        model = TemplateEmail
        fields = (
            'id',
            'user',
            'name',
            'body',
            'created_at'
        )

    def to_representation(self, instance: TemplateEmail) -> dict:
        from trainer.serializers.user import UserSerializer

        data = super(TemplateEmailSerializer, self).to_representation(instance)

        data.update({
            'user': UserSerializer(instance=instance.user).data,
        })

        return data
