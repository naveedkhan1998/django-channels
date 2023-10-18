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

# Final stage for the smaller image
FROM python:3.9-alpine

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the built dependencies from the builder stage
COPY --from=builder /usr/local /usr/local

# Create and set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Collect static files (if applicable)
RUN python manage.py collectstatic 

# Run Django on all available network interfaces
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

RUN chmod +x /app/start.sh
ENTRYPOINT ["./start.sh"]