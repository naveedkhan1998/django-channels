# Use the Python Alpine image as the base image
FROM python:3.9-alpine

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk add --update --no-cache \
    build-base \
    libffi-dev \
    openssl-dev

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Collect static files (if applicable)
RUN python manage.py collectstatic --noinput

# Run Django on all available network interfaces
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
