# Employee Management System

A REST API built with Python, Django REST Framework, JWT authentication and PostgreSQL support. It provides employee CRUD operations, search, ordering and admin-controlled write access.

## Features

- JWT login and token refresh endpoints
- Create, list, retrieve, update and delete employee records
- Search employees by name, email, ID, department or job title
- Ordering by name, joining date or creation date
- Admin-only create, update and delete; authenticated users can read
- PostgreSQL configuration through environment variables
- SQLite fallback for quick local setup

## Tech stack

Python · Django · Django REST Framework · Simple JWT · PostgreSQL · Git

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/employee-management-system.git
cd employee-management-system
```

### 2. Create and activate a virtual environment

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

For a quick start, leave `.env` absent and the project uses SQLite.

For PostgreSQL, create a database, copy `.env.example` to `.env`, then update `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` and `DB_PORT`. Set a strong `SECRET_KEY` before deployment. Never commit `.env`.

### 5. Run migrations and create an admin

```bash
python manage.py makemigrations employees
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/admin/` for the Django admin.

## API endpoints

All employee endpoints require a valid JWT access token.

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/token/` | Obtain access and refresh tokens |
| POST | `/api/auth/token/refresh/` | Refresh access token |
| GET | `/api/employees/` | List employees |
| POST | `/api/employees/` | Create employee (admin only) |
| GET | `/api/employees/{id}/` | Retrieve employee |
| PUT/PATCH | `/api/employees/{id}/` | Update employee (admin only) |
| DELETE | `/api/employees/{id}/` | Delete employee (admin only) |

### Get a token

Send a POST request to `/api/auth/token/`:

```json
{
  "username": "your-admin-username",
  "password": "your-admin-password"
}
```

Use the returned access token in the request header:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### Create an employee (admin token)

Send a POST request to `/api/employees/`:

```json
{
  "username": "jane.doe",
  "password": "StrongPassword123!",
  "employee_id": "EMP-001",
  "full_name": "Jane Doe",
  "email": "jane@example.com",
  "department": "Engineering",
  "job_title": "Python Developer",
  "phone": "+91-9000000000",
  "date_joined": "2025-01-15",
  "is_active": true
}
```

### Search and ordering

- `/api/employees/?search=jane`
- `/api/employees/?search=Engineering`
- `/api/employees/?ordering=full_name`
- `/api/employees/?ordering=-date_joined`

## Notes

- This is a portfolio starter project. Review security settings, add automated tests, pagination, audit logging and production deployment configuration before using it with real employee data.
- Do not commit credentials, `.env` files, database dumps or real personal information.
