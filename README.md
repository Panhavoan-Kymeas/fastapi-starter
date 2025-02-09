
# FastAPI Starter Project

This is a starter project for building APIs with FastAPI. It includes:

- SQLite for development (easily switchable to other databases).
- Authentication and user management.
- Alembic for database migrations.
- Pytest for testing.

## Features

- **Modular Structure**: The project is organized into `core`, `apps`, `tests`, and other directories for better maintainability.
- **SQLite by Default**: SQLite is used for development, but you can easily switch to PostgreSQL, MySQL, or another database.
- **Authentication**: Includes password hashing and JWT-based authentication.
- **Testing**: Comes with a basic test suite using `pytest`.

## Setup

1. **Clone the Repository**  
   If you haven't already cloned the repository, do so using:

   ```bash
   git clone https://github.com/yourusername/fastapi-starter.git
   cd fastapi-starter
   ```

2. **Create a Virtual Environment**  
   To isolate your project's dependencies, create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**  
   Activate the virtual environment based on your operating system:

- **On Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **On macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

Once activated, you should see `(venv)` in your terminal prompt.

4. **Install Dependencies**  
   Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements/dev.txt
   ```

5. **Set Up the Database**  
   The project uses SQLite by default. To initialize the database:

   1. **Import all Models into `env.py` for Alembic**  
      For Alembic to detect your models, you must import them in `env.py`. This is crucial for migration to work.  
      Example:

      ```python
      # In env.py, import models like this:
      from apps.users.models import User  # Add imports for all models
      ```

   2. **Run the following command to apply migrations:**

      ```bash
      alembic upgrade head
      ```

      This will create the necessary tables in the SQLite database (`dev.db`).

6. **Run the Application**  
   Start the FastAPI application using Uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

   The `--reload` flag enables hot-reloading during development, so changes to your code will automatically restart the server.

   Visit `http://127.0.0.1:8000/docs` in your browser to access the interactive API documentation (Swagger UI).

7. **Run Tests**  
   To run the test suite, use:

   ```bash
   pytest
   ```

8. **Deactivate the Virtual Environment**  
   When you're done working on the project, deactivate the virtual environment:

   ```bash
   deactivate
   ```

## Switching Databases

To switch from SQLite to another database (e.g., PostgreSQL), update the `DATABASE_URL` in the `.env` file. For example:

```bash
DATABASE_URL=postgresql://user:password@localhost/dbname
```

Then, re-run the migrations:

```bash
alembic upgrade head
```

## Project Structure

```
.
├── core                # Core functionality (config, database, security)
├── apps                # Application modules (e.g., users)
│   └── users           # User-related models, schemas, routes, and services
├── tests               # Test suite
├── migrations          # Alembic migration scripts
├── requirements        # Dependency files
├── .env                # Environment variables
├── alembic.ini         # Alembic configuration
├── main.py             # Application entry point
└── README.md           # This file
```

## Notes

- **Virtual Environment**: Always activate the virtual environment before running the application or installing new dependencies.
- **Dependencies**: If you add new packages, update the `requirements/base.txt` or `requirements/dev.txt` file and re-run:

  ```bash
  pip install -r requirements/dev.txt
  ```

- **Environment Variables**: Ensure sensitive information (like database credentials) is stored in the `.env` file, which is ignored by Git.
- **Alembic Migrations**: Always ensure all your models are imported into `env.py` for Alembic to detect and apply the necessary migrations. Failing to do so will result in migrations not reflecting the latest changes to the models.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Make sure to follow the existing code style and structure.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
