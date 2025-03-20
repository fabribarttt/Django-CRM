# 📌 Proyecto CRM en Django

Este es un **CRM (Customer Relationship Management) desarrollado en Django**, que permite gestionar registros de clientes de manera sencilla.

## ✨ Funcionalidades

- 🔐 **Inicio de sesión y registro de usuarios**
- 📋 **Agregar, visualizar, actualizar y eliminar registros**
- 🛠️ **Mejoras en la estructura y organización del código**

El desarrollo se basó en el proyecto de **Codemy**, pero con algunos ajustes y mejoras en la organización del código.

Este proyecto fue realizado como parte de mi aprendizaje en Django. 🚀

---

## 🚀 Cómo Probar la Aplicación

1️⃣ Clonar el repositorio

```sh
git clone https://github.com/fabribarttt/Django-CRM.git
cd repositorio
```

2️⃣ Crear un entorno virtual

```sh
# En Windows
python -m venv venv

# En macOS/Linux
python3 -m venv venv
```

3️⃣ Activar el entorno virtual

```sh
# En Windows
venv\Scripts\activate

# En macOS/Linux
source venv/bin/activate
```

4️⃣ Instalar las dependencias

```sh
pip install -r requirements.txt
```

5️⃣ Aplicar migraciones y crear la base de datos

Para generar la base de datos, es necesario tener **SQLite** instalado en tu sistema (generalmente ya viene preinstalado con Python).

```sh
python manage.py migrate
```

6️⃣ Crear un superusuario (opcional, para acceder al panel de administración)

```sh
python manage.py createsuperuser
```

Crear un superusuario es opcional, pero necesario si deseas acceder al panel de administración de Django.

7️⃣ Ejecutar el servidor

```sh
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000/`.

---
