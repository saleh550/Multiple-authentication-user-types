# Django Multiple Authentication User Types 

## Overview

This project is a Django-based user management system that supports three distinct user roles: Teacher, Student, and Visitor. Each user role has unique fields and functionalities, and the system uses JWT (JSON Web Tokens) for authentication via the `rest_framework_simplejwt` package.

## Features

- **Custom User Model**: A single user model extended to support different roles.
- **Role-Specific Models**: Separate models for Teachers, Students, and Visitors with unique fields.
- **Registration Endpoints**: Dedicated endpoints for each user role to handle registration.
- **JWT Authentication**: Secure authentication using JSON Web Tokens.
- **Profile Retrieval**: Endpoint to retrieve user profile details based on the authenticated user's token.

## User Roles

### Teacher
- **Fields**: `subject`
- **Registration Endpoint**: `/api/teacher/register/`
- **Profile Endpoint**: `/api/profile/`

### Student
- **Fields**: `average`
- **Registration Endpoint**: `/api/student/register/`
- **Profile Endpoint**: `/api/profile/`

### Visitor
- **Fields**: Additional visitor-specific fields can be added.
- **Registration Endpoint**: `/api/visitor/register/`
- **Profile Endpoint**: `/api/profile/`

## Endpoints

### Registration Endpoints

- **Teacher Registration**
  - **URL**: `/api/teacher/register/`
  - **Method**: POST
  - **Body**:
    ```json
    {
        "user": {
            "username": "teacher_username",
            "password": "securepassword123",
            "role": "teacher"
        },
        "subject": "Mathematics"
    }
    ```

- **Student Registration**
  - **URL**: `/api/student/register/`
  - **Method**: POST
  - **Body**:
    ```json
    {
        "user": {
            "username": "student_username",
            "password": "securepassword123",
            "role": "student"
        },
        "average": 85.5
    }
    ```

- **Visitor Registration**
  - **URL**: `/api/visitor/register/`
  - **Method**: POST
  - **Body**:
    ```json
    {
        "user": {
            "username": "visitor_username",
            "password": "securepassword123",
            "role": "visitor"
        }
    }
    ```

### Authentication Endpoint

- **Token Obtain**
  - **URL**: `/api/token/`
  - **Method**: POST
  - **Body**:
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
  - **Response**:
    ```json
    {
        "refresh": "your_refresh_token",
        "access": "your_access_token",
        "role": "your_role"
    }
    ```

### Profile Endpoint

- **Get Profile Details**
  - **URL**: `/api/profile/`
  - **Method**: GET
  - **Headers**: `Authorization: Bearer <your_jwt_token>`
  - **Response** (example for a teacher):
    ```json
    {
        "user": {
            "username": "teacher_username",
            "email": "teacher@example.com",
            "first_name": "First",
            "last_name": "Last",
            "role": "teacher"
        },
        "subject": "Mathematics"
    }
    ```

## Setup and Installation

1. **Clone the repository**:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

4. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

5. **Access the application**:
    Open your web browser and go to `http://localhost:8000/`.

## Testing

To test the registration and profile retrieval, you can use tools like `curl`, Postman, or httpie to send HTTP requests to the endpoints mentioned above.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
