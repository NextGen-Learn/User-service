![Скриншот 1](screenshots/Screenshot%20from%202024-09-24%2020-31-18.png)
![Скриншот 2](screenshots/Screenshot%20from%202024-09-24%2020-32-18.png)

```markdown
# User Service API 🚀

## Project Description

This project is an API for managing users and mentors. It provides functionalities for creating, reading, updating, and deleting user data and their relationships with mentors. 🌟

## Technologies Stack

- Python 3.9 🐍
- Django 🌐
- Django REST Framework 📦
- drf-yasg (for API documentation) 📜
- PostgreSQL (or another database system) 🗄️

## Installation

### Prerequisites

- Docker 🐳
- Docker Compose (optional) ⚙️

### Build and Run the Project using Docker

1. Clone the repository:
   ```bash
   git clone git@github.com:NextGen-Learn/User-service.git
   ```

2. Navigate to the project directory:
   ```bash
   cd User-service
   ```

3. Build and run the container:
   ```bash
   docker build -t user-service .
   docker run -p 8001:8001 user-service
   ```

4. Open your browser and go to `http://localhost:8001/` to access the API. 🌐

### Database Setup

If you are using PostgreSQL, ensure that you have set up a database for the project and updated the connection parameters in `settings.py`. 🔧

## Using the API

You can access the API through the following endpoints:

- **Swagger UI**: [http://localhost:8001/swagger/](http://localhost:8001/swagger/) 📊
- **ReDoc**: [http://localhost:8001/redoc/](http://localhost:8001/redoc/) 📚
- **JSON Schema**: [http://localhost:8001/swagger.json/](http://localhost:8001/swagger.json/) ⚡

### Endpoints

To get information about available endpoints and how to use them, please refer to Swagger UI or ReDoc, which are automatically generated based on your code. 📝

## API Documentation

The documentation for your API is available at the following addresses:

- **Swagger UI**: An interface with documentation and endpoint testing. 🎤
- **ReDoc**: A beautiful interface with your API documentation in OpenAPI format. 🌈

## Testing

To run tests, execute the command:

```bash
python manage.py test
```

## Contributing

If you would like to contribute to the project, please create a fork of the repository and submit a pull request with your changes. 🤝