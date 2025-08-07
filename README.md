# 🚀 QuickTask Pro - Multi-Tenant Task Management System

**QuickTask Pro** is a multi-tenant SaaS task management system built using Django & Django REST Framework. 
It allows organizations to manage projects, assign tasks, and monitor progress—complete with role-based access and secure authentication.

---

## 🧩 Features

- ✅ **Multi-Tenant**: Isolated data per organization.
- 👤 **User Roles**: `admin`, `manager`, and `member` with custom permissions.
- 🔐 **JWT Authentication** via `SimpleJWT`.
- 📁 **Project & Task Management** with audit logging.
- 🔍 **Search & Filter** support for task listings.
- 🧪 **Modular Codebase** with clean serializers, views, and signals.

---

## 📦 Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (SimpleJWT)
- **Database**: SQLite (for local development)
- **Env Management**: `python-decouple`
- **Hosting Ready**: Can be deployed to platforms like Render --> https://quicktaskpro-2.onrender.com

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
https://github.com/snehasivadas21/quicktaskpro.git
cd quicktask

python -m venv env
env\Scripts\activate --- on Windows

POST /register/              -> Register a new user
POST /token/                 -> Get access and refresh token
POST /token/refresh/         -> Refresh your access token

GET /organization/          - List organizations
POST /organization/         - Create organization

GET /projects/              - List projects
POST /projects/             - Create a project

GET /projects/              - List projects
POST /projects/             - Create a project

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


