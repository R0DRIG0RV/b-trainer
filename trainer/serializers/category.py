from rest_framework.serializers import ModelSerializer
from trainer.models.category import Category

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'order'
        )