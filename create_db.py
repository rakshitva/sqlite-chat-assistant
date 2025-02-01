import sqlite3

def create_database():
    # Connect to SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()
    
    # Create the Employees table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            ID INTEGER PRIMARY KEY,
            Name TEXT,
            Department TEXT,
            Salary INTEGER,
            Hire_Date TEXT
        )
    ''')

    # Create the Departments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Departments (
            ID INTEGER PRIMARY KEY,
            Name TEXT,
            Manager TEXT
        )
    ''')

    # Insert sample data into Employees table
    cursor.execute('INSERT OR IGNORE INTO Employees (ID, Name, Department, Salary, Hire_Date) VALUES (1, "Alice", "Sales", 50000, "2021-01-15")')
    cursor.execute('INSERT OR IGNORE INTO Employees (ID, Name, Department, Salary, Hire_Date) VALUES (2, "Bob", "Engineering", 70000, "2020-06-10")')
    cursor.execute('INSERT OR IGNORE INTO Employees (ID, Name, Department, Salary, Hire_Date) VALUES (3, "Charlie", "Marketing", 60000, "2022-03-20")')

    # Insert sample data into Departments table
    cursor.execute('INSERT OR IGNORE INTO Departments (ID, Name, Manager) VALUES (1, "Sales", "Alice")')
    cursor.execute('INSERT OR IGNORE INTO Departments (ID, Name, Manager) VALUES (2, "Engineering", "Bob")')
    cursor.execute('INSERT OR IGNORE INTO Departments (ID, Name, Manager) VALUES (3, "Marketing", "Charlie")')

    conn.commit()
    conn.close()

create_database()
