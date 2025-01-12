# Alx_Final_Project
# Movie Review API

A robust and scalable Movie Review API built using Django and Django REST Framework (DRF). This application allows users to perform CRUD operations for movie reviews, manage user accounts, and access various advanced features like authentication, pagination, sorting, and more.

---

## Features

- **CRUD Operations**: Create, Read, Update, and Delete movie reviews.
- **User Management**: User registration, login, and profile management.
- **Authentication**: Secure endpoints using JWT authentication.
- **Pagination**: Efficient handling of large datasets with pagination.

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Django 4.0+
- Django REST Framework
- SQLite (development purposes)
- bootstrap4 (for front-end integrations)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/oritsamuel/Alx_Final_Project.git
   cd mymovie
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   source env/bin/activate 
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database settings in `settings.py`:

   

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the API at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).

---

## API Endpoints

### Authentication

- **POST** `/api/auth/register/`: Register a new user.
- **POST** `/api/auth/login/`: Log in and obtain a JWT token.

### Movies

- **GET** `/api/movies/`: List all movies.
- **POST** `/api/movies/`: Add a new movie (Admin only).

### Reviews

- **GET** `/api/reviews/`: List all reviews.
- **POST** `/api/reviews/`: Add a new review.
- **PUT** `/api/reviews/{id}/`: Update a review.
- **DELETE** `/api/reviews/{id}/`: Delete a review.


---

## Deployment

1. Set up a production environment using services like Heroku.
2. Configure `settings.py` for production (e.g., `DEBUG=False`).
3. Set up a WSGI server like Gunicorn and serve static files using a CDN.

---





## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

