from rest_framework.serializers import ModelSerializer
from trainer.models.client_document import ClientDocument


class ClientDocumentSerializer(ModelSerializer):

    class Meta:
        model = ClientDocument
        fields = (
            'id',
            'client',
            'document'
        )

    def to_representation(self, instance: ClientDocument) -> dict:
        from trainer.serializers.category import CategorySerializer
        from trainer.serializers.document import DocumentSerializer

        data = super(ClientDocumentSerializer, self).to_representation(instance)

        data.update({
            'client': CategorySerializer(instance=instance.client).data,
            'document': DocumentSerializer(instance=instance.document).data,
        })

        return data