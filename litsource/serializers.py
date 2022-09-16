from rest_framework.serializers import ModelSerializer
from .models import LitSource


class LitSourceSerializer(ModelSerializer):
    class Meta:
        model = LitSource
        fields = '__all__'
        read_only_fields = ['id', 'source_type']
