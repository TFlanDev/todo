# Full Stack Todo Application

A full-stack web app built with **Django REST Framework** on the backend and **React** on the frontend. It lets users register, log in, and manage their own personal todo lists with full CRUD functionality.

---

## Project Overview

This project is split into two parts — a Django backend that provides the REST API and a React frontend that serves as the client.

## Technology Stack

### Backend

* **Framework:** Django + Django REST Framework
* **Authentication:** JSON Web Tokens (JWT) using Simple JWT
* **Database:** SQLite 
* **CORS Handling:** `django-cors-headers`

### Frontend

* **Framework:** React (Vite setup)
* **Routing:** React Router
* **HTTP Client:** Axios
* **Token Management:** jwt-decode

---

## Features

* **User Accounts:** Register, log in, and get secure JWT tokens for authentication
* **Todo Management:** Create, read, update, and delete your own tasks
* **Access Control:** Each user only sees their own todos
* **Modern Stack:** React frontend separated cleanly from Django API
* **Easy Setup:** Simple configuration with environment variables

---

## Getting Started

### Requirements

* Python 3.10 or higher
* Node.js (with npm or yarn)
* A virtual environment (recommended)

### Backend Setup

1. Go to the backend folder:

   ```bash
   cd backend
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the backend root:

   ```
   DJANGO_SECRET_KEY='your-secret-key'
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the Django server:

   ```bash
   python manage.py runserver
   ```

   The backend will run at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install axios react-router-dom jwt-decode
   ```

3. Start the development server:

   ```bash
   npm run dev
   ```

   The frontend will run at **[http://localhost:5173](http://localhost:5173)**

---

## API Endpoints

| Method               | Endpoint               | Description                                 |
| :------------------- | :--------------------- | :------------------------------------------ |
| **POST**             | `/api/user/register/`  | Create a new user                           |
| **POST**             | `/api/token/`          | Get an access token                         |
| **POST**             | `/api/token/refresh/`  | Refresh an expired access token             |
| **GET, POST**        | `/api/todos/`          | List or create todos for the logged-in user |
| **GET, PUT, DELETE** | `/api/todos/<int:pk>/` | Retrieve, update, or delete a specific todo |

---

## Notes

* All API routes except user registration require authentication.

---

## Future Improvements

* Add password reset and email verification
* Implement dark mode in the frontend
* Add tags or priority levels for todos
* Deploy to a live demo environment

---

**Author:** Thomas Flanley
**License:** MIT
