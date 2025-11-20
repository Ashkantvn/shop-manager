# Shop Manager

A Django-based product management system with real-time WebSocket notifications and comprehensive testing.

## 🚀 Features

- **Product Management** - Create, read, update, and delete products
- **Real-time Notifications** - WebSocket-based live updates for product changes
- **User Authentication** - Secure login system with staff/admin roles
- **Dashboard** - Live product change feed for staff members
- **PostgreSQL Database** - Reliable persistent data storage
- **Redis Integration** - Channel layer support for WebSocket broadcasts
- **Comprehensive Tests** - Pytest with async support and coverage
- **Code Quality** - Flake8 linting and Black formatting

## 📋 Prerequisites

- Docker & Docker Compose
- Python 3.10+ (for local development)
- PostgreSQL 16
- Redis 7.2

## 🛠️ Installation & Setup

### Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd shop-manager
   ```

2. **Create environment file**
   ```bash
   mkdir -p env
   # Copy and configure env/.env.dev with your settings
   ```

3. **Build and start services**
   ```bash
   docker compose -f docker-compose.dev.yml up -d
   ```

4. **Run migrations**
   ```bash
   docker compose -f docker-compose.dev.yml exec django python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   docker compose -f docker-compose.dev.yml exec django python manage.py createsuperuser
   ```

### Local Development Setup

1. **Create virtual environment**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp env/.env.dev.example env/.env.dev
   # Edit env/.env.dev with your settings
   ```

4. **Run migrations**
   ```bash
   cd core
   python manage.py migrate
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

## 📁 Project Structure

```
shop-manager/
├── core/                          # Django project root
│   ├── core/                      # Project settings & ASGI
│   │   ├── settings/
│   │   │   ├── base.py           # Base configuration
│   │   │   └── dev.py            # Development settings
│   │   ├── asgi.py               # ASGI application with WebSocket routing
│   │   └── urls.py               # URL routing
│   │
│   ├── accounts/                 # User authentication app
│   │   ├── views.py              # Login/logout views
│   │   ├── urls.py
│   │   └── tests/
│   │
│   ├── products/                 # Product management app
│   │   ├── models/
│   │   │   └── product.py        # Product model with slug field
│   │   ├── views/
│   │   │   ├── product_list_delete.py
│   │   │   ├── product_create.py  # CreateView with authentication
│   │   │   └── product_detail.py  # DetailView with update capability
│   │   ├── signals.py            # Product change signals
│   │   ├── utils.py              # Helper functions & notify
│   │   ├── urls.py
│   │   └── tests/
│   │       ├── test_product_views.py
│   │       ├── test_urls.py
│   │       └── test_models.py
│   │
│   ├── dashboard/                # Real-time dashboard app
│   │   ├── consumers.py          # WebSocket consumer
│   │   ├── router.py             # WebSocket URL routing
│   │   ├── views.py              # Dashboard view
│   │   ├── urls.py
│   │   └── tests/
│   │       └── test_dashboard.py
│   │
│   ├── templates/                # HTML templates
│   │   ├── layout.html           # Base template
│   │   ├── 404.html
│   │   ├── accounts/
│   │   ├── products/
│   │   └── dashboard/
│   │
│   ├── static/                   # Static files
│   │   └── js/
│   │       └── dashboard.js      # WebSocket client
│   │
│   ├── conftest.py               # Pytest fixtures
│   └── manage.py
│
├── docker-compose.dev.yml        # Docker Compose configuration
├── Dockerfile.dev
├── requirements.txt              # Python dependencies
└── README.md
```

## 🔌 API Endpoints

### Products
- `GET /products/` - List all products
- `GET /products/<slug>/` - Get product details
- `POST /products/<slug>/` - Update product (authenticated)
- `GET /products/create/` - Show create form (authenticated)
- `POST /products/create/` - Create product (authenticated)
- `GET /products/<slug>/delete` - Confirm delete (authenticated)
- `POST /products/<slug>/delete` - Delete product (authenticated)

### Authentication
- `GET /accounts/login/` - Login page
- `POST /accounts/login/` - Submit login form
- `GET /accounts/logout/` - Logout user

### Dashboard
- `GET /dashboard/products/` - Real-time product updates (authenticated, staff only)

### WebSocket
- `ws://localhost:8000/ws/products/` - WebSocket endpoint for product notifications (authenticated, staff/superuser only)

## 🔄 Real-time Updates (WebSocket)

The application uses Django Channels to broadcast product changes in real-time to connected clients.

**Flow:**
1. Product is created/updated/deleted
2. Django signal (`post_save`, `post_delete`) is triggered
3. Signal calls `notify_product_changes()` to send message to WebSocket group
4. Connected clients receive message and display it on dashboard

**Connected clients see:**
- Product created events
- Product updated events with detailed field changes
- Product deleted events

## 🧪 Running Tests

```bash
# Run all tests
docker compose -f docker-compose.dev.yml exec django pytest

# Run specific test file
docker compose -f docker-compose.dev.yml exec django pytest products/tests/test_product_views.py

# Run with coverage
docker compose -f docker-compose.dev.yml exec django pytest --cov=products

# Run specific test
docker compose -f docker-compose.dev.yml exec django pytest products/tests/test_product_views.py::TestProductViews::test_GET_product_list_200
```

## 📊 Code Quality

```bash
# Run Flake8 linting
docker compose -f docker-compose.dev.yml exec django flake8

# Format code with Black
docker compose -f docker-compose.dev.yml exec django black core/
```

## 🔐 User Roles

- **Superuser** - Full access to admin panel and all features
- **Staff** - Can access dashboard and manage products
- **Regular User** - Can only view products

## 🌳 Environment Variables

Required in `.env.dev`:
```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

POSTGRES_DB=shop_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=postgres
DB_PORT=5432

REDIS_URL=redis://redis:6379/0
```

## 📦 Key Dependencies

- **Django 5.2.8** - Web framework
- **Django Channels** - WebSocket support
- **Daphne** - ASGI server
- **PostgreSQL** - Database
- **Redis** - Message broker for channels
- **Pytest** - Testing framework
- **Black** - Code formatter
- **Flake8** - Linter

## 🚀 Production Deployment

For production:
1. Set `DEBUG=False` in settings
2. Use environment-specific settings file
3. Configure proper `ALLOWED_HOSTS`
4. Use Gunicorn + Daphne with reverse proxy (Nginx)
5. Enable HTTPS/SSL
6. Configure PostgreSQL backup strategy
7. Set up Redis persistence

## 📝 License

MIT License

## 👤 Author

ashkantvn
