# Event Manager

This project is aimed at creating a simple Event Manager using Python. The application allows users to create, delete, and edit events, including descriptions and other relevant details. The project utilizes Docker for containerization and MongoDB for the database.

## Project Structure

- **Documentation**: Contains project-related documents such as design specifications, user manuals, etc.
- **Source Code**: Holds all the Python source code files for the application.
- **Tests**: Includes test scripts and files for testing the application functionality.

## Getting Started

To run the Event Manager on your local machine, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone <repository_url>
    ```
2. **Navigate to the source code directory**:
    ```sh
    cd sourcecode
    ```
3. **Build and run the Docker containers**:
    ```sh
    docker-compose up --build
    ```
4. **Access the application** by navigating to the appropriate URL (usually `http://localhost:5000`).

## Features

- Create, delete, and edit events.
- Store event details such as description, date, and time.
- MongoDB integration for data persistence.
- Docker containerization for easy setup and deployment.
- User-friendly interface for managing events.

## Contributors

No contributors, all projects were done by me ([GitHub](https://github.com/1shushi1)).

## License

This project is licensed under the MIT License.
