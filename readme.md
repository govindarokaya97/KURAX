# KURAX — Django News Portal

KURAX is a full-stack news/blog platform built with **Django**. It ships three layers in one codebase:

- 🌐 **Public site** — a magazine-style front end (home, category/tag pages, search, post detail, comments, contact form, newsletter signup)
- 🛠️ **Admin/editor panel** (`/news-admin/`) — a custom CMS for authenticated staff to create, edit, and publish posts as drafts before they go live
- 🔌 **REST API** (`/api/v1/`) — a Django REST Framework API exposing posts, categories, tags, and users, with a separate draft-publish endpoint

## Features

- Draft → Publish workflow (posts stay hidden from the public site until `published_at` is set)
- Category and tag browsing with popularity-based navigation (trending posts, popular tags/categories)
- Full-text post search
- Threaded comments per post
- Contact form and newsletter subscription capture
- View-count tracking per post
- User registration for the admin panel
- REST API with browsable DRF interface, session + basic authentication

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0 |
| API | Django REST Framework |
| Database | SQLite (default, dev) |
| Images | Pillow |
| Frontend | Django templates (HTML/CSS/JS theme) |

## Project Structure

```
KURAX/
├── News/            # Project settings, root urls, WSGI
├── news_app/        # Public-facing site: models, views, forms, navigation context
├── blog_app/        # Admin/editor panel (news-admin): CRUD + draft/publish views
├── api/              # DRF app: serializers, viewsets, API routes
├── templates/        # HTML templates (kurax, panel, lists, details, registration, admin)
├── static/            # CSS/JS/image assets
├── media/             # User-uploaded post & profile images
└── manage.py
```

## Data Model

- **Post** — title, content, image, author, category (FK), tags (M2M), status (`active`/`in_active`), `published_at` (null = draft), view count
- **Category**, **Tag** — simple taxonomy models
- **Comment** — linked to a Post
- **Contact**, **Newsletter** — form submissions
- **UserProfile** — extended profile info per user

## Getting Started

### Prerequisites

- Python 3.12+
- pip

### Installation

```bash
# Clone the repo
git clone https://github.com/<your-username>/KURAX.git
cd KURAX

# Create and activate a virtual environment
python -m venv env
source env/bin/activate      # Windows: env\Scripts\activate

# Install dependencies
pip install django djangorestframework pillow

# Apply migrations
python manage.py migrate

# Create an admin/editor account
python manage.py createsuperuser

# Run the dev server
python manage.py runserver
```

Then visit:

- `http://127.0.0.1:8000/` — public site
- `http://127.0.0.1:8000/news-admin/` — editor panel (login required)
- `http://127.0.0.1:8000/admin/` — Django admin
- `http://127.0.0.1:8000/api/v1/` — browsable REST API

## API Overview

Base URL: `/api/v1/`

| Endpoint | Methods | Auth | Notes |# KURAX — Django News Portal

KURAX is a full-stack news/blog platform built with **Django**. It ships three layers in one codebase:

- 🌐 **Public site** — a magazine-style front end (home, category/tag pages, search, post detail, comments, contact form, newsletter signup)
- 🛠️ **Admin/editor panel** (`/news-admin/`) — a custom CMS for authenticated staff to create, edit, and publish posts as drafts before they go live
- 🔌 **REST API** (`/api/v1/`) — a Django REST Framework API exposing posts, categories, tags, and users, with a separate draft-publish endpoint

## Features

- Draft → Publish workflow (posts stay hidden from the public site until `published_at` is set)
- Category and tag browsing with popularity-based navigation (trending posts, popular tags/categories)
- Full-text post search
- Threaded comments per post
- Contact form and newsletter subscription capture
- View-count tracking per post
- User registration for the admin panel
- REST API with browsable DRF interface, session + basic authentication

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0 |
| API | Django REST Framework |
| Database | SQLite (default, dev) |
| Images | Pillow |
| Frontend | Django templates (HTML/CSS/JS theme) |

## Project Structure

```
KURAX/
├── News/            # Project settings, root urls, WSGI
├── news_app/        # Public-facing site: models, views, forms, navigation context
├── blog_app/        # Admin/editor panel (news-admin): CRUD + draft/publish views
├── api/              # DRF app: serializers, viewsets, API routes
├── templates/        # HTML templates (kurax, panel, lists, details, registration, admin)
├── static/            # CSS/JS/image assets
├── media/             # User-uploaded post & profile images
└── manage.py
```

## Data Model

- **Post** — title, content, image, author, category (FK), tags (M2M), status (`active`/`in_active`), `published_at` (null = draft), view count
- **Category**, **Tag** — simple taxonomy models
- **Comment** — linked to a Post
- **Contact**, **Newsletter** — form submissions
- **UserProfile** — extended profile info per user

## Getting Started

### Prerequisites

- Python 3.12+
- pip

### Installation

```bash
# Clone the repo
git clone https://github.com/<your-username>/KURAX.git
cd KURAX

# Create and activate a virtual environment
python -m venv env
source env/bin/activate      # Windows: env\Scripts\activate

# Install dependencies
pip install django djangorestframework pillow

# Apply migrations
python manage.py migrate

# Create an admin/editor account
python manage.py createsuperuser

# Run the dev server
python manage.py runserver
```

Then visit:

- `http://127.0.0.1:8000/` — public site
- `http://127.0.0.1:8000/news-admin/` — editor panel (login required)
- `http://127.0.0.1:8000/admin/` — Django admin
- `http://127.0.0.1:8000/api/v1/` — browsable REST API

## API Overview

Base URL: `/api/v1/`

| Endpoint | Methods | Auth | Notes |
|---|---|---|---|
| `posts/` | GET | Public | List/detail limited to published, active posts |
| `posts/` | POST/PUT/PATCH/DELETE | Required | Manage posts |
| `categories/` | GET, POST, PUT, PATCH, DELETE | Required | |
| `tags/` | GET, POST, PUT, PATCH, DELETE | Required | |
| `users/`, `groups/` | GET, POST, PUT, PATCH, DELETE | Required | |
| `post-publish/` | POST | Required | Publishes a draft: `{"post": <id>}`. Only works on posts where `published_at` is still null. |
| `api-auth/` | — | — | DRF's login/logout for the browsable API |

Authentication uses DRF's default **Session** and **Basic** authentication. For quick testing in Postman, use Basic Auth with a valid user's username/password.

## Known Limitations / Notes for Production

This project is configured for local development out of the box:

- `SECRET_KEY` is hardcoded in `settings.py` — replace and load from an environment variable before deploying
- `DEBUG = True` and `ALLOWED_HOSTS = []` — update both for production
- SQLite is used as the default database — swap for PostgreSQL/MySQL in production

## Credits

The public-facing front-end theme is adapted from a template by [Colorlib](https://colorlib.com/wp/templates/), used under their [license terms](https://colorlib.com/wp/licence/).

## Author

**Govinda Rokaya (Spyro)**
GitHub: [@GovindaRokaya](https://github.com/GovindaRokaya)
|---|---|---|---|
| `posts/` | GET | Public | List/detail limited to published, active posts |
| `posts/` | POST/PUT/PATCH/DELETE | Required | Manage posts |
| `categories/` | GET, POST, PUT, PATCH, DELETE | Required | |
| `tags/` | GET, POST, PUT, PATCH, DELETE | Required | |
| `users/`, `groups/` | GET, POST, PUT, PATCH, DELETE | Required | |
| `post-publish/` | POST | Required | Publishes a draft: `{"post": <id>}`. Only works on posts where `published_at` is still null. |
| `api-auth/` | — | — | DRF's login/logout for the browsable API |

Authentication uses DRF's default **Session** and **Basic** authentication. For quick testing in Postman, use Basic Auth with a valid user's username/password.

## Known Limitations / Notes for Production

This project is configured for local development out of the box:

- `SECRET_KEY` is hardcoded in `settings.py` — replace and load from an environment variable before deploying
- `DEBUG = True` and `ALLOWED_HOSTS = []` — update both for production
- SQLite is used as the default database — swap for PostgreSQL/MySQL in production

## Credits

The public-facing front-end theme is adapted from a template by [Colorlib](https://colorlib.com/wp/templates/), used under their [license terms](https://colorlib.com/wp/licence/).

## Author

**Govinda Rokaya (Spyro)**
GitHub: [@GovindaRokaya](https://github.com/GovindaRokaya)
