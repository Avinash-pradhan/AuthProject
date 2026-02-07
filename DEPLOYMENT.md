# AuthProject Deployment Guide

This document provides instructions for deploying AuthProject to Render using the Blueprint.

## Quick Start on Render

1. **Connect Your Repository**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New +" → "Blueprint"
   - Select your GitHub repository (Avinash-pradhan/AuthProject)
   - Select the `main` branch

2. **Review Blueprint Configuration**
   - The `render.yaml` file will be auto-detected
   - Review the services:
     - **Database**: PostgreSQL (starter plan)
     - **Web Service**: Python 3.12 Django app with gunicorn
   - Click "Create New Blueprint"

3. **Deploy**
   - Render will:
     - Provision PostgreSQL database
     - Install dependencies from `requirements.txt`
     - Run migrations: `python manage.py migrate`
     - Collect static files: `python manage.py collectstatic --noinput`
     - Start the app with gunicorn
   - Your app will be live at `https://authproject.onrender.com` (or similar)

## Environment Variables

Render automatically sets:

- `DATABASE_URL` - PostgreSQL connection string
- `SECRET_KEY` - Auto-generated for security
- `DEBUG` - Set to `False` for production
- `ALLOWED_HOSTS` - Configured for `*.onrender.com`

## Local Development

1. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Create `.env` File**

   ```bash
   cp .env.example .env
   ```

3. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

4. **Create Superuser**

   ```bash
   python manage.py createsuperuser
   ```

5. **Start Dev Server**
   ```bash
   python manage.py runserver
   ```

## Password Reset in Development

When you request a password reset:

- Emails are printed to the console (configured via `EMAIL_BACKEND`)
- Look in the terminal for the reset link
- Format: `http://127.0.0.1:8000/reset/<uid>/<token>/`

## Files for Deployment

- `render.yaml` - Blueprint configuration
- `Procfile` - Process definitions
- `requirements.txt` - Python dependencies with gunicorn, dj-database-url, whitenoise
- `AuthProject/settings.py` - Updated for environment variables and static file handling

## Troubleshooting

### Build Fails

- Check `requirements.txt` has all needed packages
- Ensure `gunicorn` and `dj-database-url` are listed
- Verify no syntax errors in `render.yaml`

### Static Files Not Loading

- WhiteNoise is configured for production
- Run `python manage.py collectstatic` locally to test
- Ensure `STATIC_ROOT = BASE_DIR / 'staticfiles'` in settings

### Database Connection Issues

- Render auto-injects `DATABASE_URL`
- Settings.py automatically uses `dj_database_url.config()`
- No manual DATABASE_URL configuration needed

### Create Admin User on Render

After first deployment:

```bash
# Via Render shell (if available)
python manage.py createsuperuser
```

Or use Django admin to create staff users via the web interface.

## Updating Your Blueprint

- Future edits to `render.yaml` on the `main` branch will auto-sync
- Changes take effect on next deploy
- Manual redeploy: Click "Redeploy" in Render dashboard
