# User Registration API

This is a simple FastAPI application that provides endpoints for user sign-up. It includes a Docker setup for easy deployment.

## Features

- User sign-up endpoint
- PostgreSQL database integration
- Dockerized for easy deployment

## Installation

1. Clone this repository to your local machine.
2. Make sure you have Docker installed.
3. Navigate to the project directory in your terminal.

## Usage

### Running Locally

To run the application locally without Docker, follow these steps:

1. Ensure you have Python 3.12 installed.
2. Install dependencies using Poetry:

    ```
    poetry install
    ```

3. Create the necessary database tables:

    ```
    poetry run python sign_up/main.py
    ```

4. Run the FastAPI server:

    ```
    poetry run uvicorn sign_up.main:app --host 0.0.0.0 --reload
    ```

5. Access the API at [http://localhost:8000](http://localhost:8000) in your browser or via API client.

### Running with Docker

To run the application using Docker, follow these steps:

1. Ensure you have Docker installed and running.
2. Navigate to the project directory in your terminal.
3. Run the following command to build the Docker image:

    ```
    docker-compose build
    ```

4. After the build is complete, start the Docker containers:

    ```
    docker-compose up
    ```

5. Access the API at [http://localhost:8000](http://localhost:8000) in your browser or via API client.

## API Documentation

- **GET /**: Root endpoint, returns "Hello World".
- **POST /users/**: Endpoint for user sign-up.

## Configuration

- PostgreSQL database details can be configured in the `docker-compose.yml` file.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

