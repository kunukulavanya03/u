## u Backend API

### Overview

u is a platform built with React as the frontend and FastAPI + SQLAlchemy as the backend.

### API Endpoints

#### Health Check

* `GET /health`: Returns the status of the API.

#### Users

* `GET /users`: Returns a list of all users.
* `POST /users`: Creates a new user.
* `GET /users/{user_id}`: Returns a user by ID.
* `PUT /users/{user_id}`: Updates a user.
* `DELETE /users/{user_id}`: Deletes a user.

### Authentication

* `POST /token`: Returns a JWT token for authentication.

### Environment Variables

* `DATABASE_URL`: The URL of the database.
* `SECRET_KEY`: The secret key for JWT tokens.
* `ACCESS_TOKEN_EXPIRE_MINUTES`: The expiration time of JWT tokens in minutes.
* `ALGORITHM`: The algorithm used for JWT tokens.

### Running the API

1. Install the dependencies with `pip install -r requirements.txt`.
2. Create a `.env` file with the environment variables.
3. Run the API with `uvicorn app.main:app --host 0.0.0.0 --port 8000`.

### Testing the API

1. Run the tests with `pytest tests`.