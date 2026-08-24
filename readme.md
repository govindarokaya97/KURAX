# 📰 KURAX — Django News Portal

> **KURAX** is a full-stack, magazine-style news and blogging platform built with **Django** and **Django REST Framework**. It combines a public news website, a custom content-management panel, and a RESTful API in a single Django project.


---

## 📌 Project Overview

KURAX is a modern digital news and blogging platform designed for publishing, managing, and discovering news content.

The platform provides a complete publishing workflow where authenticated editors can create and manage articles as drafts, review content, and publish approved articles to the public website.

Visitors can browse published news, explore categories and tags, search for articles, read detailed stories, comment on posts, subscribe to newsletters, and contact the KURAX team.

The project consists of three major layers:

* 🌐 **Public News Website**
* 🛠️ **Custom News Administration Panel**
* 🔌 **REST API**

---

# ✨ Features

## 🌐 Public News Website

The public-facing KURAX website provides:

* 🏠 Homepage
* 📰 Latest news
* 🔥 Trending news
* 🗂️ Category-based browsing
* 🏷️ Tag-based navigation
* 🔎 Article search
* 📖 Article detail pages
* 💬 Threaded comments
* 👁️ Post view counting
* 📩 Contact form
* 📬 Newsletter subscription
* 📱 Responsive design
* 🌤️ Date and local time display
* 🌦️ Weather information
* 🔗 Social media navigation
* 🖼️ Featured article images
* 📊 Popular content sections

---

# 🛠️ Custom News Administration Panel

KURAX includes a custom content-management panel available at:

```text
/news-admin/
```

Authenticated staff can:

* Create articles
* Edit articles
* Delete articles
* Save articles as drafts
* Publish articles
* Manage categories
* Manage tags
* Upload article images
* Manage user profiles
* Review content
* Monitor draft and published content

The custom panel provides a cleaner workflow for editors without requiring them to work directly with Django's default administration interface.

---

# 🔌 REST API

KURAX provides a RESTful API through:

```text
/api/v1/
```

The API is built with **Django REST Framework**.

It provides endpoints for:

* Posts
* Categories
* Tags
* Users
* Groups
* Post publishing
* API authentication

The API also provides a browsable interface for easier development and testing.

---

# 🚀 Key Features at a Glance

| Feature              | Description                           |
| -------------------- | ------------------------------------- |
| 📰 News Management   | Create, edit and manage news articles |
| 📝 Draft Workflow    | Save articles before publishing       |
| 🚀 Publishing        | Publish approved articles             |
| 🗂️ Categories       | Organize articles into categories     |
| 🏷️ Tags             | Add multiple tags to articles         |
| 🔥 Trending News     | Display popular/trending content      |
| 🔎 Search            | Search articles by title/content      |
| 💬 Comments          | Comment and reply to articles         |
| 👁️ View Counter     | Track article views                   |
| 📩 Contact           | Capture visitor messages              |
| 📬 Newsletter        | Capture newsletter subscribers        |
| 👤 Profiles          | Store additional user information     |
| 🖼️ Media Uploads    | Upload article/profile images         |
| 🔌 REST API          | Programmatic access to content        |
| 🔐 Authentication    | Protect editor/API operations         |
| 📱 Responsive UI     | Desktop, tablet and mobile support    |
| 🌤️ Live Information | Date, time and weather display        |

---

# 🖥️ Project Preview

## KURAX Branding

![KURAX Logo](static/kurax/assets/img/logo/logo1.png)

The KURAX logo is used throughout the public-facing website and represents the primary project branding.

---

## Homepage

The KURAX homepage follows a magazine-style news layout containing:

* Trending news
* Featured articles
* Recent news
* Category navigation
* Popular content
* Social media section
* Newsletter/contact sections
* Responsive article cards

### Example Homepage Content

Current content includes categories such as:

* ⚽ Football
* 🏛️ Politics
* 💰 Economy
* ✈️ Travel
* 💻 Science & Technology
* 👥 Society
* 💭 Opinion

---

# 📰 News Cards

KURAX uses article images throughout the homepage, category pages, and article detail pages.

Example project media structure:

```text
media/
└── post_images/
    ├── 2026/
    │   ├── 08/
    │   │   ├── 07/
    │   │   │   ├── nirmal-purja-1024x500-1.jpg
    │   │   │   ├── WhatsApp-Image-2026-07-20-at-11.42.22-AM.jpeg
    │   │   │   ├── dhiraj-seth-1024x500-1.png
    │   │   │   └── wire_tar_ktm-8-1024x683-1.jpg
    │   │   │
    │   │   ├── 10/
    │   │   │   ├── ANFA-nepal-2.png
    │   │   │   ├── Parking-fee-Kathmandu.jpg
    │   │   │   └── Jyoti-ranabhat-1230-1024x624-1.jpg
    │   │   │
    │   │   └── 21/
    │   │       └── Swarnim-Wagle-4_JoRcbXJ.jpg
```

These images help visually separate different types of news content.

---

# 🎨 Branding & Static Assets

The main KURAX logo is stored at:

```text
static/kurax/assets/img/logo/logo1.png
```

The general static asset structure is:

```text
static/
└── kurax/
    └── assets/
        ├── css/
        ├── js/
        ├── img/
        │   ├── logo/
        │   ├── hero/
        │   ├── news/
        │   └── ...
        └── fonts/
```

Static files contain application/theme assets, while uploaded content is stored separately in the `media/` directory.

---

# 🏗️ Application Architecture

KURAX follows a modular Django architecture.

```text
                         ┌──────────────────────┐
                         │      KURAX USER      │
                         └──────────┬───────────┘
                                    │
                   ┌────────────────┼────────────────┐
                   │                │                │
                   ▼                ▼                ▼
            ┌─────────────┐  ┌──────────────┐  ┌─────────────┐
            │ Public Site │  │ Admin Panel  │  │ REST API    │
            │             │  │ /news-admin/ │  │ /api/v1/    │
            └──────┬──────┘  └──────┬───────┘  └──────┬──────┘
                   │                │                 │
                   └────────────────┼─────────────────┘
                                    ▼
                           ┌──────────────────┐
                           │  Django Models   │
                           └────────┬─────────┘
                                    │
                                    ▼
                           ┌──────────────────┐
                           │ SQLite Database  │
                           └──────────────────┘
```

---

# 📁 Project Structure

```text
KURAX/
│
├── News/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── news_app/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── context_processors.py
│
├── blog_app/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
│
├── api/
│   ├── migrations/
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   ├── kurax/
│   ├── panel/
│   ├── registration/
│   ├── lists/
│   ├── details/
│   └── admin/
│
├── static/
│   └── kurax/
│       └── assets/
│
├── media/
│   └── post_images/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🗄️ Data Model

The core KURAX data model consists of:

* `User`
* `UserProfile`
* `Post`
* `Category`
* `Tag`
* `Comment`
* `Contact`
* `Newsletter`

Conceptually:

```text
                         User
                          │
                          ▼
                    UserProfile
                          │
                          ▼
                        Author
                          │
                          │
                          ▼
Category ─────────────── Post ─────────────── Tags
                          │
                          │
                          ▼
                       Comments


Contact

Newsletter
```

---

# 📰 Post Model

A post contains information such as:

* Title
* Content
* Featured image
* Author
* Category
* Tags
* Status
* Published date
* View count

The post publication system separates draft content from publicly visible content.

---

# 🔄 Draft → Publish Workflow

KURAX uses a draft-to-publish workflow.

```text
                  Create Article
                        │
                        ▼
                 ┌─────────────┐
                 │    Draft    │
                 └──────┬──────┘
                        │
                  Editor Review
                        │
                        ▼
                 ┌─────────────┐
                 │  Published  │
                 └──────┬──────┘
                        │
                        ▼
                  Public Website
```

A post remains hidden from the public website until it is published.

The publishing logic uses:

```text
status = active
AND
published_at IS NOT NULL
```

This allows editors to prepare and review content without immediately exposing it to visitors.

---

# 📊 Content Discovery

KURAX provides several ways for visitors to discover content.

## Categories

Examples include:

* Football
* Politics
* Economy
* Travel
* Science & Technology
* Society
* Opinion

## Tags

Tags provide a more granular way to organize related articles.

## Trending

Popular content can be surfaced in the trending section.

## Latest News

The latest published content is displayed in chronological order.

## Search

Visitors can search articles using the site's search functionality.

---

# 💬 Comments

KURAX supports comments associated with individual articles.

The comment structure supports threaded discussions:

```text
Post
 │
 ├── Comment
 │    ├── Reply
 │    └── Reply
 │
 └── Comment
      ├── Reply
      └── Reply
```

This allows readers to participate in discussions around published stories.

---

# 👁️ View Tracking

Each article maintains a view count.

View statistics can help identify:

* Popular articles
* Trending stories
* High-interest categories
* Content performance

---

# 📩 Contact System

Visitors can contact the KURAX team through the contact form.

Submitted information can be captured by the backend for review and response.

---

# 📬 Newsletter

KURAX provides a newsletter subscription feature.

Visitors can submit their email addresses to subscribe to future news and updates.

---

# 🔌 REST API

Base URL:

```text
/api/v1/
```

## API Endpoints

| Endpoint        | Methods                   | Authentication    | Purpose                          |
| --------------- | ------------------------- | ----------------- | -------------------------------- |
| `posts/`        | GET                       | Public            | Retrieve published posts         |
| `posts/`        | POST                      | Required          | Create a post                    |
| `posts/`        | PUT/PATCH                 | Required          | Update a post                    |
| `posts/`        | DELETE                    | Required          | Delete a post                    |
| `categories/`   | GET                       | Public/Configured | Retrieve categories              |
| `categories/`   | POST                      | Required          | Create category                  |
| `categories/`   | PUT/PATCH                 | Required          | Update category                  |
| `categories/`   | DELETE                    | Required          | Delete category                  |
| `tags/`         | GET                       | Public/Configured | Retrieve tags                    |
| `tags/`         | POST                      | Required          | Create tag                       |
| `tags/`         | PUT/PATCH                 | Required          | Update tag                       |
| `tags/`         | DELETE                    | Required          | Delete tag                       |
| `users/`        | GET/POST/PUT/PATCH/DELETE | Required          | User management                  |
| `groups/`       | GET/POST/PUT/PATCH/DELETE | Required          | Group management                 |
| `post-publish/` | POST                      | Required          | Publish a draft                  |
| `api-auth/`     | Login/Logout              | Session           | DRF browsable API authentication |

---

# 🚀 Publish a Post Through API

Endpoint:

```text
POST /api/v1/post-publish/
```

Request:

```json
{
    "post": 11
}
```

The endpoint publishes a post that has not already been assigned a `published_at` value.

---

# 🔐 API Authentication

The project uses Django REST Framework authentication.

Supported mechanisms include:

* Session Authentication
* Basic Authentication

For example, API testing can be performed using Postman.

```text
Authorization
Type: Basic Auth

Username: your_username
Password: your_password
```

---

# 🌐 Main Application Routes

## Public Website

### Homepage

```text
/
```

### Latest News

```text
/post-list/
```

### Article Detail

```text
/detail/<id>/
```

### Category

```text
/post-by-category/<id>/
```

### About

```text
/about/
```

### Contact

```text
/contact/
```

---

# 🛠️ Administration Routes

### KURAX Custom Admin

```text
/news-admin/
```

### Django Administration

```text
/admin/
```

---

# 🔌 API Root

```text
/api/v1/
```

---

# 🛠️ Technology Stack

| Layer                | Technology                                 |
| -------------------- | ------------------------------------------ |
| Backend              | Django 6.0                                 |
| Programming Language | Python 3.12+                               |
| API                  | Django REST Framework                      |
| Database             | SQLite                                     |
| Image Processing     | Pillow                                     |
| Frontend             | HTML5, CSS3, JavaScript                    |
| Templates            | Django Templates                           |
| Styling              | Bootstrap / Custom CSS                     |
| Authentication       | Django Authentication + DRF Authentication |
| API Testing          | Postman / DRF Browsable API                |
| Version Control      | Git & GitHub                               |

---

# ⚙️ Installation

## Prerequisites

Before running KURAX, install:

* Python 3.12 or newer
* pip
* Git

---

## 1. Clone the Repository

```bash
git clone https://github.com/GovindaRokaya/KURAX.git
```

Move into the project directory:

```bash
cd KURAX
```

---

## 2. Create a Virtual Environment

### Windows

```powershell
python -m venv env
```

Activate it:

```powershell
env\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv env
```

Activate it:

```bash
source env/bin/activate
```

---

## 3. Install Dependencies

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

Otherwise:

```bash
pip install django djangorestframework pillow
```

---

## 4. Apply Database Migrations

```bash
python manage.py migrate
```

---

## 5. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create the administrator account.

---

## 6. Collect Static Files

For deployment or production-like testing:

```bash
python manage.py collectstatic
```

---

## 7. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

---

# 🌍 Application URLs

| Application           | URL                                 |
| --------------------- | ----------------------------------- |
| 🌐 Public Website     | `http://127.0.0.1:8000/`            |
| 🛠️ KURAX Admin Panel | `http://127.0.0.1:8000/news-admin/` |
| ⚙️ Django Admin       | `http://127.0.0.1:8000/admin/`      |
| 🔌 REST API           | `http://127.0.0.1:8000/api/v1/`     |

---

# 🖼️ Static & Media Files

KURAX separates static application assets from user-uploaded media.

## Static Files

```text
static/
└── kurax/
    └── assets/
        ├── css/
        ├── js/
        ├── img/
        │   ├── logo/
        │   ├── hero/
        │   ├── news/
        │   └── ...
        └── fonts/
```

The primary KURAX logo is:

```text
static/kurax/assets/img/logo/logo1.png
```

## Uploaded Media

```text
media/
└── post_images/
```

Uploaded article images are stored under date-based directories.

This separation provides a clean distinction:

```text
static/
    → Theme, CSS, JavaScript, logos and application assets

media/
    → User-uploaded article/profile content
```

---

# 📱 Responsive Design

KURAX is designed as a responsive news portal.

The UI is intended to support:

* 💻 Desktop
* 💻 Laptop
* 📱 Mobile
* 📲 Tablet

The primary page flow is:

```text
Top Information Bar
        ↓
Main Header
        ↓
Navigation
        ↓
Trending News
        ↓
Featured News
        ↓
Recent News
        ↓
Category News
        ↓
Social Media
        ↓
Footer
```

---

# 🌤️ Date, Time & Weather

The top information bar provides contextual information such as:

```text
TODAY
Monday, 24 Aug 2026

LOCAL TIME
06:55 PM

WEATHER
Current weather information
```

The interface is designed to display the visitor's local date/time and weather information.

If weather data is unavailable, the frontend should gracefully display an appropriate fallback message instead of leaving the user with a permanent loading state.

---

# 📈 Content Management Workflow

The overall editorial workflow is:

```text
Editor Login
     │
     ▼
Create Article
     │
     ▼
Add Category
     │
     ▼
Add Tags
     │
     ▼
Upload Image
     │
     ▼
Save as Draft
     │
     ▼
Review
     │
     ▼
Publish
     │
     ▼
Public Website
```

This workflow provides a basic CMS experience inside the Django application.

---

# 🧪 Development Commands

## Check Django Configuration

```bash
python manage.py check
```

## Create Migrations

```bash
python manage.py makemigrations
```

## Apply Migrations

```bash
python manage.py migrate
```

## Create Superuser

```bash
python manage.py createsuperuser
```

## Run Tests

```bash
python manage.py test
```

## Run Development Server

```bash
python manage.py runserver
```

## Collect Static Files

```bash
python manage.py collectstatic
```

---

# 🔒 Security & Production Considerations

The default configuration is intended primarily for development and demonstration.

Before deploying KURAX to production, review the following configuration.

## Environment Variables

Sensitive values should be moved from source code into environment variables.

Recommended configuration includes:

```text
SECRET_KEY
DEBUG
ALLOWED_HOSTS
DATABASE_URL
```

---

## Disable Debug Mode

Production environments should use:

```python
DEBUG = False
```

---

## Configure Allowed Hosts

Set appropriate production domains:

```python
ALLOWED_HOSTS = [
    "yourdomain.com",
    "www.yourdomain.com",
]
```

---

## Production Database

SQLite is convenient for development.

For production deployments, PostgreSQL is recommended.

```text
Development
     ↓
SQLite

Production
     ↓
PostgreSQL
```

---

## HTTPS

Production deployment should use HTTPS.

Also configure:

* Secure cookies
* CSRF protection
* HSTS
* Secure session cookies
* Security headers

---

# 🖼️ Image Management Recommendations

For production, uploaded images should be optimized before serving.

Recommended improvements include:

* Image compression
* Thumbnail generation
* WebP/AVIF conversion
* Maximum upload dimensions
* File-type validation
* File-size validation
* CDN integration
* Cloud storage

---

# 🚀 Future Improvements

KURAX provides a strong foundation for additional features.

Potential future improvements include:

* 🔔 Browser notifications
* ❤️ Article likes
* 🔖 Save/bookmark articles
* 👤 Reader accounts
* 🧑‍💼 Advanced editor roles
* 📊 Analytics dashboard
* 📰 RSS feeds
* 📧 Automated newsletters
* 🔍 Advanced PostgreSQL search
* 🖼️ Automatic image optimization
* 🌙 Dark mode
* 🌐 Multi-language support
* 📱 Progressive Web App
* ☁️ Cloud media storage
* 🚀 Docker deployment
* 🔄 CI/CD pipeline
* 📈 SEO optimization
* 🗺️ Sitemap generation
* 🤖 Structured metadata / Open Graph support

---

# 📊 Suggested Production Architecture

A future production deployment could use:

```text
                         Internet
                            │
                            ▼
                    ┌───────────────┐
                    │ Nginx / Proxy │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Gunicorn      │
                    │ Django        │
                    └───────┬───────┘
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
       PostgreSQL       Redis/Cache    Media Storage
```

This architecture would provide a stronger foundation for production traffic and scalability.

---

# 📚 API Development

The REST API can be consumed by:

* Postman
* Frontend applications
* Mobile applications
* Third-party integrations
* JavaScript clients
* Future React/Vue/Angular applications

The API architecture keeps the backend content layer separate from the presentation layer.

---

# 🎯 Project Goals

KURAX was developed to demonstrate practical implementation of:

* Django application architecture
* Django ORM
* Model relationships
* Class-based views
* Django templates
* Form handling
* Authentication
* CRUD operations
* Media handling
* Content publishing workflows
* Django REST Framework
* API authentication
* Git/GitHub workflow
* Responsive frontend integration

---

# 💡 What KURAX Demonstrates

The project demonstrates how Django can be used to build a complete content-driven platform rather than only a simple CRUD application.

It combines:

```text
Frontend
   +
Django Backend
   +
Database
   +
Authentication
   +
CMS
   +
REST API
   +
Media Management
   +
Content Workflow
```

into one integrated application.

---

# 🙏 Credits

The public-facing news theme was adapted from a **Colorlib** template.

Original theme provider:

**Colorlib**

Third-party theme assets remain subject to their respective licenses and terms of use.

---

# 👨‍💻 Author

## Govinda Rokaya

**Backend Django Developer**

GitHub:

**[@GovindaRokaya](https://github.com/GovindaRokaya)**

Project:

**KURAX — Django News Portal**

---

# 📄 License

This project is intended for:

* Educational purposes
* Portfolio demonstration
* Learning
* Development

Third-party assets and theme components remain subject to their respective licenses.

---

# ⭐ KURAX

### A complete Django-powered news publishing platform.

**Create. Edit. Review. Publish. Discover.**

![KURAX Logo](static/kurax/assets/img/logo/logo1.png)
