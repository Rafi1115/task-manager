# Django Task Manager

A simple Django task management application with user authentication and CRUD operations for tasks.

## Table of Contents

- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration](#configuration)
  - [Environment Variables](#environment-variables)
  - [Database Setup](#database-setup)
- [Documentation](#documentation)
  - [Running the Project](#running-the-project)
  - [API Endpoints](#api-endpoints)

## Setup

### Prerequisites

- Python 3.x
- Django
- PostgreSQL
- mailtrap.io

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/django-task-manager.git
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

### Environment Variables

Create a `.env` file in the `task_manager` folder and add the following environment variables:

```plaintext
SECRET_KEY=''
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
DB_PORT=''

EMAIL_HOST=''
EMAIL_PORT=''
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD=''
```
## Update

Before proceeding, ensure you have created a `.env` file in the `task_manager` folder with the following environment variables:

```plaintext
SECRET_KEY=''
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
DB_PORT=''

EMAIL_HOST=''
EMAIL_PORT=''
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD=''
```
### Database Setup

Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```
### Documentation
Running the Project
```python manage.py runserver```
The project will be accessible at http://127.0.0.1:8000/tasks/.

## API Endpoints
The API provides the following endpoints:
```
List Tasks: GET /api/tasks/
Retrieve Task: GET /api/tasks/{task_id}/
Create Task: POST /api/tasks/
Update Task: PUT /api/tasks/{task_id}/
Delete Task: DELETE /api/tasks/{task_id}/

```
Make requests using your preferred API client (e.g., Postman).

Remember to populate the ```.env``` file and create ```media``` folder at the root, set up the database, and apply migrations before running the project.
