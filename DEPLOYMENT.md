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

**You MUST set these for password reset emails to work:**

- `EMAIL_HOST` - SMTP server (e.g., `smtp.gmail.com`)
- `EMAIL_PORT` - SMTP port (e.g., `587`)
- `EMAIL_USE_TLS` - Use TLS (e.g., `True`)
- `EMAIL_HOST_USER` - Your email address
- `EMAIL_HOST_PASSWORD` - Your email password or app-specific password
- `DEFAULT_FROM_EMAIL` - Sender email for password reset

### Setting Up Email on Render

1. Go to your Render service dashboard
2. Click "Environment" → "Add Secret"
3. Add each email variable above
4. For Gmail: Use an [App Password](https://support.google.com/accounts/answer/185833), NOT your main password
5. Redeploy the service

Without these, password reset emails will fail!

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

## Security Configuration (Automatic on Render)

When `DEBUG=False` (production), the following are enabled:

- `SECURE_SSL_REDIRECT=True` - All requests redirect to HTTPS
- `SESSION_COOKIE_SECURE=True` - Sessions only via HTTPS
- `CSRF_COOKIE_SECURE=True` - CSRF tokens only via HTTPS
- `SECURE_HSTS_SECONDS=31536000` - HTTP Strict Transport Security for 1 year
- `CSRF_TRUSTED_ORIGINS` - Configured for Render domains

These are automatically applied when deployed to Render (DEBUG=False by render.yaml).

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

### Email / Password Reset Not Working

**Problem:** Password reset emails don't arrive or crash

**Solution:**

1. Ensure all `EMAIL_*` environment variables are set in Render (see "Setting Up Email on Render" above)
2. For Gmail: Generate an [App Password](https://support.google.com/accounts/answer/185833) and use that, not your main password
3. Test locally: `python manage.py shell` → `from django.core.mail import send_mail` → `send_mail(...)`
4. Check Render logs for SMTP errors: Dashboard → Logs tab

Example Gmail setup:

```
EMAIL_HOST = smtp.gmail.com
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = your-gmail@gmail.com
EMAIL_HOST_PASSWORD = xxxx xxxx xxxx xxxx  # 16-char App Password
```

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
