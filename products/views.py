from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from products.models import Product
from products.serializers import ProductSerializer


class ProductApiViewSet(ModelViewSet):
    """
    CRUD de Productos (Unidad 1).
    Permite lectura pública y modificación por usuarios autenticados.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
