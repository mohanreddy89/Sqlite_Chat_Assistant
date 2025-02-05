# Sqlite_Chat_Assistant
# Chat Assistant API

This project implements a chat assistant API using FastAPI and SQLite. The API allows users to query information about employees stored in an SQLite database.

## Table of Contents

- Installation
- Usage
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Project Structure](#project-structure)
- Contributing

## Installation

1. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
2. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
3. **Ensure the SQLite database is set up: Run the database_setup.py script to create the company.db database and the Employees table if they do not already exist.**
   ```sh
   python database_setup.py

**Usage:**
       **1. Run the FastAPI server:**
       ```sh
       uvicorn chat_assistant:app --reload
       **2. Access the API documentation: Open your browser and navigate to 
            http://127.0.0.1:8000/docs to view the interactive API documentation provided by 
            Swagger UI.**
**API Endpoints:**

POST /chat
This endpoint allows users to query information about employees.

      ```sh
      Request Body:
      
      {
        "query": "all employees in <department>"
      }
      
      Response:
      
      200 OK: Returns a list of employee names in the specified department.
      400 Bad Request: Returns an error message if the query is invalid.

**Example request:**
      ```sh
      curl -X 'POST' \
        'http://127.0.0.1:8000/chat' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "query": "all employees in Sales"
      }'

**Database Schema:**
The Employees table has the following schema:

ID (INTEGER PRIMARY KEY): A unique identifier for each employee.
Name (TEXT NOT NULL): The name of the employee.
Department (TEXT NOT NULL): The department the employee belongs to.
Salary (INTEGER): The salary of the employee.
Hire_Date (TEXT): The date the employee was hired.

**Project Structure:**
chat-assistant-api/
│
├── database_setup.py       # Script to set up the SQLite database
├── chat_assistant.py       # Main FastAPI application
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
└── company.db              # SQLite database file (created by database_setup.py)

**Contributing
Contributions are welcome! Please follow these steps:**

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
