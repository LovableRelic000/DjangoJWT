from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'stock', 'active', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
