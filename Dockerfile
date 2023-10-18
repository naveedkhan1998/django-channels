# Use the Python Alpine image as the base image for the first stage
FROM python:3.9-alpine AS builder

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk add --no-cache --virtual .build-deps \
    build-base \
    libffi-dev \
    openssl-dev

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code into the container
COPY . .

# Collect static files (if applicable)
RUN python manage.py collectstatic --noinput

# Wait for the database to be ready
RUN python manage.py wait_for_db

# Create new database migration files based on model changes
RUN python manage.py makemigrations

# Apply database migrations to the database
RUN python manage.py migrate --noinput

# Create an admin user if it doesn't exist
RUN python manage.py initadmin

# Start your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
