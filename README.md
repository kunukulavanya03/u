# u

Backend API for u

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Designpythonworldclockui.git))

## Project Structure

```
u/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- user registration
- user login
- password reset
- profile management
- resource management

## API Endpoints

- `POST /api/register` - Register a new user account.
- `POST /api/login` - Log in to an existing user account.
- `POST /api/password_reset` - Reset a user's password.
- `GET /api/profile` - Get a user's profile information.
- `PUT /api/profile` - Update a user's profile information.
- `GET /api/resources` - Get a list of available resources.
- `POST /api/resources` - Create a new resource.
- `PUT /api/resources/{resource_id}` - Update an existing resource.
- `DELETE /api/resources/{resource_id}` - Delete a resource.

## License

MIT
