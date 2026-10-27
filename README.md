# TechStore API - Backend Django REST Framework & JWT

API RESTful desarrollada con **Django** y **Django REST Framework (DRF)** que implementa autenticación mediante **JSON Web Tokens (JWT)**, gestión de usuarios personalizados (sustituyendo username por email) y catálogo de productos (Unidad 1), documentada interactivamente con **Swagger / OpenAPI**.

---

## 📋 Requerimientos y Adaptaciones Implementadas

### 1. Nombre y Tema Propio
* El proyecto no utiliza el nombre "restaurante".
* Se configuró con el nombre **TechStore API**, reflejado tanto en la configuración interna de Django como en el título y descripción de **Swagger UI**.

### 2. Modelo de Usuario Personalizado con Campo Extra
* Modelo `User` heredado de `AbstractUser` configurado en `settings.AUTH_USER_MODEL = 'users.User'`.
* El identificador principal de login es el campo `email` (`USERNAME_FIELD = 'email'`).
* **Campo extra:** Se agregó el campo `telefono` (`CharField max_length=20`).
* El campo `telefono` se encuentra integrado y visible en:
  - **Panel de Administración de Django** (listado `list_display` y formulario de edición `fieldsets`).
  - **Serializador** (`UserSerializer`).
  - **Swagger / OpenAPI** (esquemas y documentación de endpoints).

### 3. Configuración de Tiempo de Vida del Token
* Configurado explícitamente en `techstore/settings.py` dentro de `SIMPLE_JWT`:
  - `ACCESS_TOKEN_LIFETIME = timedelta(minutes=60)` (60 minutos de vigencia).
  - `REFRESH_TOKEN_LIFETIME = timedelta(days=1)` (1 día de vigencia).

---

## 🔒 Corrección de Fallas de Seguridad del Manual

| Falla en el Manual | Riesgo de Seguridad | Solución Implementada |
| :--- | :--- | :--- |
| **1. Exposición del hash de contraseña** en las respuestas de la API (`/users/`, `/auth/me/`). | Fuga de credenciales criptográficas que permite ataques de diccionario o fuerza bruta offline. | Se configuró `extra_kwargs = {'password': {'write_only': True, 'required': False}}` en `UserSerializer`. La contraseña jamás se retorna en ningún JSON de respuesta. |
| **2. Sobreescritura de contraseña en `partial_update`** si no se envía password (`request.data['password'] = request.user.password`). | La contraseña del usuario editado era reemplazada silenciosamente por el hash del administrador que realizaba la petición HTTP. | Se eliminó `request.user.password`. Ahora, si no se envía contraseña en la petición `PATCH`, la contraseña del usuario permanece completamente intacta. |

---

## 🚀 Instalación y Puesta en Marcha

### 1. Clonar el Repositorio
```bash
git clone https://github.com/LovableRelic000/DjangoJWT.git
cd DjangoJWT
```

### 2. Crear y Activar Entorno Virtual
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / MacOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Cargar Datos Iniciales (Usuarios y Productos)
```bash
python seed_data.py
```
> **Credenciales generadas:**
> * **Administrador:** `admin@techstore.com` | Contraseña: `Admin12345!`
> * **Usuario Cliente:** `carlos@techstore.com` | Contraseña: `Carlos2026!`

### 6. Ejecutar el Servidor
```bash
python manage.py runserver
```

---

## 📖 Documentación Interactiva de la API (Swagger UI)

Una vez iniciado el servidor, accede a:
* **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
* **ReDoc:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)
* **Panel de Administración:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🧪 Pruebas Automatizadas

El proyecto incluye una suite de pruebas automatizadas que valida los 5 requerimientos clave y las correcciones de seguridad:

```bash
python test_api_suite.py
```

### Pruebas ejecutadas:
1. **Obtención de Token:** `POST /api/v1/auth/token/` con credenciales de usuario.
2. **Vigencia del Token:** Validación de que `exp - iat == 3600` segundos (60 minutos).
3. **Endpoint de Perfil:** `GET /api/v1/auth/me/` con `Bearer <token>` verificando la presencia de `telefono` y la ausencia absoluta de `password`.
4. **Prueba de Seguridad PATCH:** Validación de que actualizar un usuario sin enviar contraseña no altera su clave original.
5. **Catálogo de Productos:** Consulta al CRUD de productos (`GET /api/v1/products/`).

