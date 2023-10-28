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

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/django-task-manager.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd django-task-manager
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

### Environment Variables

Create a `.env` file in the project root and add the following environment variables:

```plaintext```
DATABASE_URL=your_postgresql_database_url
SECRET_KEY=your_django_secret_key

## Update

Update `your_postgresql_database_url` and `your_django_secret_key` with your actual database URL and Django secret key.

### Database Setup

Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```
python manage.py migrate
Documentation
Running the Project
bash
Copy code
python manage.py runserver
The project will be accessible at http://127.0.0.1:8000/.

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

Remember to populate the .env file and create media folder at the root, set up the database, and apply migrations before running the project.
