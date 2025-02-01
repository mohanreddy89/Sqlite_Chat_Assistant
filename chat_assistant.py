from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

# Initialize FastAPI
app = FastAPI()

# Database connection function
def get_db_connection():
    conn = sqlite3.connect("company.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# Request model
class QueryRequest(BaseModel):
    query: str

# Define FastAPI route
@app.post("/chat")
async def chat(request: QueryRequest):
    query = request.query.lower().strip()  # Normalize the query
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if "all employees in" in query:
            department = query.split("in ")[-1].strip()
            print(f"Query: all employees in {department}")  # Debugging statement
            cursor.execute("SELECT Name FROM Employees WHERE Department COLLATE NOCASE = ?", (department,))
            employees = cursor.fetchall()
            result = [row["Name"] for row in employees]
            return {"response": result if result else f"No employees found in the department: {department}"}

        elif "manager of" in query:
            department = query.split("of ")[-1].strip()
            print(f"Query: manager of {department}")  # Debugging statement
            cursor.execute("SELECT Manager FROM Departments WHERE Name COLLATE NOCASE = ?", (department,))
            manager = cursor.fetchone()
            if manager:
                return {"response": manager["Manager"]}
            else:
                return {"response": f"Department not found: {department}"}

        elif "hired after" in query:
            date = query.split("after ")[-1].strip()
            print(f"Query: hired after {date}")  # Debugging statement
            cursor.execute("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
            employees = cursor.fetchall()
            result = [row["Name"] for row in employees]
            return {"response": result if result else f"No employees hired after {date}"}

        elif "total salary expense for" in query:
            department = query.split("for ")[-1].strip()
            print(f"Query: total salary expense for {department}")  # Debugging statement
            cursor.execute("SELECT SUM(Salary) AS total_salary FROM Employees WHERE Department COLLATE NOCASE = ?", (department,))
            total_salary = cursor.fetchone()
            if total_salary and total_salary["total_salary"] is not None:
                return {"response": total_salary["total_salary"]}
            else:
                return {"response": f"Department not found or no employees in: {department}"}

        else:
            return {"response": "I don't understand the query. Please try again."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

    finally:
        conn.close()

# Run the FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)