# Tradvo-Python-Programming-Challenge

# Tradvo Challenge

Tradvo Challenge is a Django-based web application that allows users to manage and test their uploaded mobile apps. The application includes functionalities like listing, adding, updating, deleting apps, uploading APK files, and running Appium tests automatically.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Docker Setup](#docker-setup)
- [Running Tests](#running-tests)
- [File Structure](#file-structure)


## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.8 or later
- Docker (optional, for containerization)
- MySQL
- Appium
- Android emulator (AVD)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/tradvo-challenge.git
   cd tradvo-challenge

2. Navigate to the project directory:
    ```bash
    cd yourproject
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Setup

necessary setup steps, such as configuring environment variables, setting up databases, or creating configuration files.


1. Create a `.env` file in the root directory with the following content:
    ```
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=your_database_url
    ```

2. Apply the migrations:
    ```bash
    python manage.py migrate
    ```


## Running the Application

Explain how to run the application:

1. Start the development server:
    ```bash
    python manage.py runserver
    ```

2. Access the application in your browser:
    ```
    http://127.0.0.1:8000/
    ```

If applicable run tests:

1. Run the tests:
    ```bash
    python manage.py test
    ```

# Tradvo-Python-Programming-Challenge

# Tradvo Challenge

Tradvo Challenge is a Django-based web application that allows users to manage and test their uploaded mobile apps. The application includes functionalities like listing, adding, updating, deleting apps, uploading APK files, and running Appium tests automatically.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Docker Setup](#docker-setup)
- [Running Tests](#running-tests)
- [File Structure](#file-structure)


## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.8 or later
- Docker (optional, for containerization)
- MySQL
- Appium
- Android emulator (AVD)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/tradvo-challenge.git
   cd tradvo-challenge

2. Navigate to the project directory:
    ```bash
    cd yourproject
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Setup

necessary setup steps, such as configuring environment variables, setting up databases, or creating configuration files.


1. Create a `.env` file in the root directory with the following content:
    ```
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=your_database_url
    ```

2. Apply the migrations:
    ```bash
    python manage.py migrate
    ```


## Running the Application

Explain how to run the application:

1. Start the development server:
    ```bash
    python manage.py runserver
    ```

2. Access the application in your browser:
    ```
    http://127.0.0.1:8000/
    ```

If applicable run tests:

1. Run the tests:
    ```bash
    python manage.py test
    ```


## Docker Setup

To run the application using Docker:

1. **Build the Docker containers:**

   Make sure you're in the project directory with the `Dockerfile` and `docker-compose.yml` files.

   ```bash
   docker-compose build