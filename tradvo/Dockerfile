# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for building Python packages
RUN apt-get update \
    && apt-get install -y \
        build-essential \
        libpq-dev \
        pkg-config \
        default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY  ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app



# Make port 8000 available to the world outside this container
EXPOSE 8000


# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]