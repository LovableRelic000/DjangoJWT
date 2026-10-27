from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo User.
    Incluye los campos estándar, el campo extra 'telefono', y asegura
    que el campo 'password' sea write_only para proteger las credenciales.
    """
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'telefono',
            'password',
            'is_active',
            'is_staff'
        ]
        extra_kwargs = {
            # CORRECCIÓN DE SEGURIDAD 1:
            # write_only=True garantiza que la contraseña / hash NUNCA aparezca
            # en las respuestas de la API (GET, POST, PUT, PATCH ni en /auth/me/).
            'password': {
                'write_only': True,
                'required': False
            }
        }
