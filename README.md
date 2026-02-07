# AuthProject

A Django authentication application with user registration, login, password reset, and admin panel features.

## Features

✅ User Registration & Signup  
✅ Email/Username Login  
✅ Password Reset with Email  
✅ Change Password  
✅ Admin Dashboard  
✅ Styled Pages (Home, About, Recent, Login, Signup)  
✅ Session Management

## Tech Stack

- **Framework**: Django 6.0
- **Database**: PostgreSQL (production), SQLite (development)
- **Server**: Gunicorn
- **Static Files**: WhiteNoise
- **Email**: Console backend (development), SMTP (configurable)

## Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/Avinash-pradhan/AuthProject.git
cd AuthProject
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure

Copy `.env.example` to `.env` and update as needed:

```bash
cp .env.example .env
```

### 3. Database & Admin

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run Locally

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

## Admin Access

- Go to http://127.0.0.1:8000/admin
- Login with superuser credentials

## Password Reset

In development, password reset links are printed to the console:

```
Content-Type: text/plain; charset="utf-8"
Subject: Password reset on 127.0.0.1:8000
...
Please go to the following page and choose a new password:
http://127.0.0.1:8000/reset/OA/d3mpi5-0738b72b987ca4d2cce/
```

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed Render deployment instructions.

### One-Click Deploy to Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Avinash-pradhan/AuthProject)

Or manually:

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New Blueprint" and select this repository
3. Render reads `render.yaml` and deploys automatically

## Project Structure

```
AuthProject/
├── authapp/              # Django app
│   ├── templates/        # HTML templates
│   ├── static/           # CSS files
│   ├── views.py          # View logic
│   ├── forms.py          # Form definitions
│   ├── models.py         # Database models
│   └── urls.py           # URL routing
├── AuthProject/          # Project config
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URL config
│   └── wsgi.py           # WSGI app
├── render.yaml           # Render Blueprint
├── Procfile              # Process definitions
└── requirements.txt      # Python dependencies
```

## Environment Variables

| Variable        | Development    | Production       |
| --------------- | -------------- | ---------------- |
| `DEBUG`         | `True`         | `False`          |
| `DATABASE_URL`  | (local SQLite) | Auto from Render |
| `SECRET_KEY`    | Dev key        | Auto-generated   |
| `ALLOWED_HOSTS` | localhost      | \*.onrender.com  |

## Features Overview

### Pages

- **Home** (`/`): Dashboard for logged-in users
- **About** (`/about`): Public info page
- **Login** (`/login`): User authentication
- **Signup** (`/signup`): New user registration
- **Change Password** (`/change_password/`): For authenticated users
- **Password Reset** (`/password_reset/`): Self-service reset

### Styling

Each page has dedicated CSS files in `authapp/static/`:

- `base.css` - Navbar & shared styles
- `home.css`, `login.css`, `signup.css`, `about.css`, etc.

## Dependencies

Key packages:

- `Django==6.0` - Web framework
- `gunicorn==25.0.2` - Production server
- `whitenoise==6.11.0` - Static file serving
- `dj-database-url==2.1.0` - Parse DATABASE_URL
- `Faker==40.1.0` - Test data generation

See `requirements.txt` for complete list.

## License

This project is open-source. Feel free to use and modify.

## Author

[Avinash Pradhan](https://github.com/Avinash-pradhan)

---

Need help? Check [DEPLOYMENT.md](DEPLOYMENT.md) or open an issue on GitHub.
