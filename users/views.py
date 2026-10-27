from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from users.models import User
from users.serializers import UserSerializer


class UserApiViewSet(ModelViewSet):
    """
    CRUD completo de usuarios gestionado por administradores.
    """
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if "password" in data and data["password"]:
            data["password"] = make_password(data["password"])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def partial_update(self, request, *args, **kwargs):
        """
        CORRECCIÓN DE SEGURIDAD 2:
        En el código original del manual:
            if "password" in request.data:
                request.data["password"] = make_password(request.data["password"])
            else:
                request.data["password"] = request.user.password  <-- FALLA CRÍTICA
        
        La falla consistía en que si se editaba un usuario sin enviar contraseña,
        el bloque 'else' le asignaba el hash de la contraseña del usuario administrador
        que realizaba la petición (request.user.password), modificando indebidamente
        la clave del usuario editado.

        Solución:
        Únicamente se encripta y actualiza la contraseña si viene explícitamente en el cuerpo
        de la petición (request.data). Si no viene, la contraseña existente permanece intacta.
        """
        data = request.data.copy()
        if "password" in data:
            if data["password"]:
                data["password"] = make_password(data["password"])
            else:
                data.pop("password", None)

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        data = request.data.copy()
        if "password" in data:
            if data["password"]:
                data["password"] = make_password(data["password"])
            else:
                data.pop("password", None)

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class UserView(APIView):
    """
    Endpoint para obtener los datos personales del usuario autenticado (GET /api/v1/auth/me/).
    CORRECCIÓN DE SEGURIDAD 1:
    La contraseña y su hash nunca se exponen al cliente, ya que en UserSerializer
    se encuentra configurada como write_only=True.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
