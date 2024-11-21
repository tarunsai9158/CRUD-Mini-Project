# Django CRUD Operations Mini-Project

This project is a simple web application demonstrating CRUD (Create, Read, Update, Delete) operations using Django. The application is designed to help beginners understand the basics of Django's functionalities.

---

## Features

- **Create**: Add new records to the database.
- **Read**: View a list of all records and detailed information for each record.
- **Update**: Modify existing records.
- **Delete**: Remove records from the database.

---

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.8 or above
- Django 4.0 or above
- SQLite (default Django database) or any other supported database
- Virtualenv (optional but recommended)

---

## Installation and Setup

Follow these steps to set up the project locally:

1. **Clone the repository**:
    ```bash
    git clone 
    cd 
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies **:
    ```bash
   pip install django
    ```

4. **Run migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Directory Structure

