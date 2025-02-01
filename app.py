from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import sqlite3
import re

app = Flask(__name__)
CORS(app, resources={r"/ask": {"origins": "http://localhost:5500"}})  # Allow only requests from localhost:3000

# Connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('company.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return "Welcome to the Chat Assistant!"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    query = data.get("query", "").lower()
    conn = get_db_connection()

    # Query handling logic
    if "list all employees" in query:
        employees = conn.execute('SELECT Name FROM Employees').fetchall()
        employee_names = [employee['Name'] for employee in employees]
        answer = f"Here are the employees: {', '.join(employee_names)}"
    
    elif "manager of the" in query:
        match = re.search(r"manager of the (\w+)", query)
        if match:
            department = match.group(1)
            manager = conn.execute('SELECT Manager FROM Departments WHERE Name LIKE ?', (f'%{department}%',)).fetchone()
            if manager:
                answer = f"The manager of the {department} department is {manager['Manager']}."
            else:
                answer = f"Sorry, I couldn't find the manager for the {department} department."
        else:
            answer = "Sorry, I couldn't understand the department name in your query."
    
    elif "list all employees in the" in query:
        match = re.search(r"list all employees in the (\w+)", query)
        if match:
            department = match.group(1)
            employees = conn.execute('SELECT Name FROM Employees WHERE Department LIKE ?', (f'%{department}%',)).fetchall()
            if employees:
                employee_names = [employee['Name'] for employee in employees]
                answer = f"Here is the list of employees in the {department} department: {', '.join(employee_names)}"
            else:
                answer = f"No employees found in the {department} department."
        else:
            answer = "Sorry, I couldn't understand the department name in your query."

    elif "salary expense of" in query:
        match = re.search(r"salary expense of the (\w+)", query)
        if match:
            department = match.group(1)
            total_salary = conn.execute('SELECT SUM(Salary) AS TotalSalary FROM Employees WHERE Department LIKE ?', (f'%{department}%',)).fetchone()
            if total_salary and total_salary['TotalSalary']:
                answer = f"The total salary expense of the {department} department is {total_salary['TotalSalary']}."
            else:
                answer = f"No salary data found for the {department} department."
        else:
            answer = "Sorry, I couldn't understand the department name in your query."

    else:
        answer = "Sorry, I couldn't understand your query. Please try again."

    conn.close()
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
