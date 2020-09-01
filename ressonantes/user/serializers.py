from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users objects api"""

    class Meta:
        model = get_user_model()
        fields = (
            'first_name', 'last_name', 'email', 'password',
            'mobile', 'is_whatsapp_mobile', 'is_ong', 'created_at'
        )
        extra_kwargs = {'password': {
            'write_only': True,
            'min_length': 9,
            'style': {'input_type': 'password'}
        }}

    def create(self, validated_data):
        """Create a valid new user and return it"""
        return get_user_model().objects.create_user(**validated_data)


class ChangeUserPasswordSerializer(serializers.Serializer):
    """Serializer for password change endpoint"""

    old_password = serializers.CharField(
        label='Senha Antiga',
        required=True, style={'input_type': 'password'}
    )
    new_password1 = serializers.CharField(
        label='Nova Senha',
        required=True, style={'input_type': 'password'}
    )
    new_password2 = serializers.CharField(
        label='Repita a Nova Senha',
        required=True, style={'input_type': 'password'}
    )
