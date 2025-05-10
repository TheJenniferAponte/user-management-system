# User Management System

This is a Flask-based API for managing users, including the ability to create, retrieve, update, and delete users. It is designed for use with an SQLite database and is intended to be used as a demonstration for basic CRUD (Create, Read, Update, Delete) operations.

## Features

- **Create**: Add new users to the database.
- **Read**: Get a list of users, with support for pagination, sorting, and filtering by username, email, role, status, and registration date.
- **Update**: Modify existing user information.
- **Delete**: Remove users from the database.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.7+
- Flask
- Flask-SQLAlchemy
- pytest (for testing)

### Clone the Repository

```bash
git clone https://github.com/yourusername/user-management-system.git
cd user-management-system
