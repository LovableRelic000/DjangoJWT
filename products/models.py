from django.db import models


class Product(models.Model):
    """
    Modelo de Producto (de la Unidad 1 - Catálogo TechStore).
    """
    title = models.CharField(max_length=255, verbose_name="Título / Nombre")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.PositiveIntegerField(default=0, verbose_name="Existencias")
    active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} (${self.price})"
