# Use an official Python runtime as a parent image
FROM python:3.9.17-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Run the command to start uWSGI
CMD ["adev", "runserver", "run_server.py", "--app-factory", "get_app", "--host", "0.0.0.0", "--port", "8080"]
