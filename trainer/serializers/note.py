from rest_framework.serializers import ModelSerializer
from trainer.models.note import Note


class NoteSerializer(ModelSerializer):

    class Meta:
        model = Note
        fields = (
            'id',
            'user',
            'client',
            'text',
            'created_at'
        )

    def to_representation(self, instance: Note) -> dict:
        from trainer.serializers.user import UserSerializer
        from trainer.serializers.client import ClientSerializer

        data = super(NoteSerializer, self).to_representation(instance)

        data.update({
            'user': UserSerializer(instance=instance.user).data,
            'client': ClientSerializer(instance=instance.client).data,
        })

        return data
