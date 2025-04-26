# Use official Python image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8080

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files
COPY . .

# Collect static files
RUN mkdir -p /app/staticfiles && python manage.py collectstatic --noinput

# Expose port from environment variable with fallback to 8080
EXPOSE ${PORT}

# Run the application with Gunicorn using the PORT environment variable
CMD exec gunicorn --bind 0.0.0.0:${PORT} project.wsgi:application
