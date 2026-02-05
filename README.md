# ToDo List (Django + DRF)

**Project**

This is a simple ToDo-list web application built with Django and Django REST Framework. It includes an `accounts` app (JWT-based authentication and RBAC utilities) and a `todo` app (task models, serializers, and views). The repo contains templates and API endpoints for managing tasks.

**Features**

- **Authentication**: JWT utilities in the `accounts` app.
- **RBAC**: Role-based access utilities and services.
- **API & Templates**: REST API endpoints and a simple HTML template for the todo UI.

**Requirements**

- Python 3.10+ (adjust if you use a different version)
- pip
- (Optional) PostgreSQL or the default SQLite3

**Setup (Windows)**

1. Activate the provided virtual environment (if using the bundled `venv1`):

```powershell
.\venv1\Scripts\Activate.ps1
```

2. Install dependencies (if a `requirements.txt` exists):

```powershell
pip install -r requirements.txt
```

Or install common packages used by this project:

```powershell
pip install django djangorestframework PyJWT psycopg2-binary
```

3. Apply migrations and create a superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server:

```powershell
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

**Running Tests**

```powershell
python manage.py test
```

**Project Structure (high level)**

- `accounts/`: authentication, serializers, views, RBAC services and middleware.
- `todo/`: models, serializers, views, decorators and permissions for todo items.
- `todolist/`: project settings, URLs and WSGI/ASGI entrypoints.

**API Endpoints (examples)**

The project exposes REST endpoints for account and todo functionality. Typical base paths include:

- `/api/accounts/` — auth and user-related endpoints (login, register, token).
- `/api/todo/` — todo list and item endpoints.

Refer to the apps' `urls.py` files for exact routes.

**Notes & Next Steps**

- If you plan to use PostgreSQL, update `todolist/settings.py` DATABASES accordingly and install `psycopg2-binary`.
- Review `accounts/jwt_utils.py` and `accounts/rbac_config.py` for authentication and permission behavior.
- Add a `requirements.txt` if you want reproducible installs.

---

Created for local development. If you want, I can add a `requirements.txt`, Dockerfile, or detailed API docs next.
