import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techstore.settings')
django.setup()

from users.models import User
from products.models import Product

def run():
    # 1. Crear Superusuario Administrador
    admin_email = 'admin@techstore.com'
    if not User.objects.filter(email=admin_email).exists():
        admin = User.objects.create_superuser(admin_email, 'Admin12345!')
        admin.first_name = 'Admin'
        admin.last_name = 'TechStore'
        admin.username = 'admin'
        admin.telefono = '555-100-2000'
        admin.save()
        print(f"Superusuario creado: {admin_email} / Admin12345!")
    else:
        print(f"El superusuario {admin_email} ya existe.")

    # 2. Crear Usuario Cliente / Normal
    user_email = 'carlos@techstore.com'
    if not User.objects.filter(email=user_email).exists():
        user = User.objects.create_user(user_email, 'Carlos2026!')
        user.first_name = 'Carlos'
        user.last_name = 'Gómez'
        user.username = 'carlosg'
        user.telefono = '555-456-7890'
        user.save()
        print(f"Usuario de prueba creado: {user_email} / Carlos2026!")
    else:
        print(f"El usuario {user_email} ya existe.")

    # 3. Crear Productos de ejemplo (Unidad 1)
    if Product.objects.count() == 0:
        Product.objects.create(
            title='Laptop ThinkPad T14s Gen 4',
            description='Potente laptop con Ryzen 7 PRO, 32GB LPDDR5X, 1TB SSD NVMe.',
            price=24999.00,
            stock=15
        )
        Product.objects.create(
            title='Mouse Inalámbrico MX Master 3S',
            description='Mouse ergonómico para productividad con sensor 8K DPI.',
            price=1999.00,
            stock=30
        )
        Product.objects.create(
            title='Monitor Curvo 34 Pulgadas UltraWide',
            description='Resolución WQHD 3440x1440 con tasa de refresco a 144Hz.',
            price=8999.50,
            stock=12
        )
        print("Productos de prueba creados.")
    else:
        print("Los productos de prueba ya existen.")

if __name__ == '__main__':
    run()
