from rest_framework.serializers import ModelSerializer
from trainer.models.document import Document


class DocumentSerializer(ModelSerializer):

    class Meta:
        model = Document
        fields = (
            'id',
            'user',
            'category',
            'name',
            'url_file',
            'created_at'
        )

    def to_representation(self, instance: Document) -> dict:
        from trainer.serializers.user import UserSerializer
        from trainer.serializers.category import CategorySerializer

        data = super(DocumentSerializer, self).to_representation(instance)

        data.update({
            'user': UserSerializer(instance=instance.user).data,
            'category': CategorySerializer(instance=instance.category).data,
        })

        return data
