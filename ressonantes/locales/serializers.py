from rest_framework.serializers import ModelSerializer
from core.models import City, Uf


class UfSerializer(ModelSerializer):
    """Serializer for UF model objects"""

    class Meta:
        model = Uf
        fields = ['id', 'acronym', 'name', 'region']


class CitySerializer(ModelSerializer):
    """Serializer for City model objects"""

    class Meta:
        model = City
        fields = ['id', 'uf', 'name']
