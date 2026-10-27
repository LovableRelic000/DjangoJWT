from django.urls import path, include
from rest_framework import routers
from products import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductApiViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]
