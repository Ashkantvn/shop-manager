# ⚡ Django Realtime Shop manager

## 📖 Overview

**Django Realtime Shop manager** is a Django project that combines three layers:

- 🧱 **Django Templates** — for server-rendered HTML pages  
- 🔌 **Django REST Framework (DRF)** — for RESTful APIs  
- ⚡ **Django Channels (ASGI + Daphne)** — for real-time communication (WebSockets)

This setup allows you to serve standard web pages, API endpoints, and live-updating components — all from the same Django project.

It also includes background task management using **Celery + Redis**, secure JWT authentication, and Docker support for deployment.

---

## 🧩 Features

- 🧑‍💻 REST API endpoints built with **DRF**
- 🖼️ Django templates for server-side rendering
- ⚡ Real-time updates using **Django Channels + Daphne**
- 🔐 JWT authentication via **SimpleJWT + session authentication**
- 🧵 Asynchronous tasks with **Celery + Redis**
- 🕒 Scheduled jobs using **django-celery-beat**
- 🧰 Code linting and formatting via **black** + **flake8**
- 🧪 Testing with **pytest** + **pytest-django**
- 🐳 Fully containerized with Docker

---

## ⚙️ Tech Stack

| Category | Technology |
|-----------|-------------|
| Framework | Django 5.2 |
| API | Django REST Framework |
| Real-Time | Channels, Daphne, Channels-Redis |
| Auth | djangorestframework-simplejwt |
| Task Queue | Celery, Redis, django-celery-beat |
| Database | PostgreSQL |
| Templates | Django Templates |
| Configuration | python-decouple |
| Testing | pytest, pytest-django |
| Code Quality | black, flake8 |
| Containerization | Docker |

---

## 🏁 License

This project is licensed under the MIT License.

