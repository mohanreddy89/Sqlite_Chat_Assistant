import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('company.db', check_same_thread=False)
cursor = conn.cursor()

# Create Employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Salary INTEGER,
    Hire_Date TEXT
)
''')

# Create Departments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Departments (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL UNIQUE,
    Manager TEXT
)
''')

# Insert initial data into Employees table
employees_data = [
    (1, 'Alice', 'Sales', 50000, '2021-01-15'),
    (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
    (3, 'Charlie', 'Marketing', 60000, '2022-03-20')
]
cursor.executemany('INSERT OR IGNORE INTO Employees (ID, Name, Department, Salary, Hire_Date) VALUES (?, ?, ?, ?, ?)', employees_data)

# Insert initial data into Departments table
departments_data = [
    (1, 'Sales', 'Alice'),
    (2, 'Engineering', 'Bob'),
    (3, 'Marketing', 'Charlie')
]
cursor.executemany('INSERT OR IGNORE INTO Departments (ID, Name, Manager) VALUES (?, ?, ?)', departments_data)

# Commit the changes and close the connection
conn.commit()
conn.close()